"""Generate MkDocs API pages from SCREAMLib's Java source declarations."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GITHUB_ROOT = ROOT.parent / "GitHub"
LIB = GITHUB_ROOT / "SCREAMLib"
JAVA_ROOT = LIB / "src" / "main" / "java"
OUTPUT = ROOT / "docs" / "reference"
COMPETITIONS = {
    "2025": GITHUB_ROOT / "4522_2025Competition",
    "2026": GITHUB_ROOT / "4522_2026Competition",
}


@dataclass
class Member:
    line: int
    signature: str
    kind: str
    docs: str


def git_sha(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def clean_javadoc(block: str) -> str:
    lines = block.splitlines()
    cleaned: list[str] = []
    for line in lines:
        line = re.sub(r"^\s*/?\*+/?\s?", "", line)
        line = re.sub(r"^\s*\*/\s*$", "", line)
        line = re.sub(r"\s*\*/\s*$", "", line)
        line = line.strip()
        if not line:
            if cleaned and cleaned[-1]:
                cleaned.append("")
            continue
        line = re.sub(r"\{@code\s+([^}]+)\}", r"`\1`", line)
        line = re.sub(r"\{@link\s+([^}]+)\}", r"`\1`", line)
        line = re.sub(r"<\s*li\s*>", "- ", line, flags=re.IGNORECASE)
        line = re.sub(r"<\s*/?\s*(p|ul|ol)\s*>", "", line, flags=re.IGNORECASE)
        line = re.sub(r"<\s*br\s*/?\s*>", "  ", line, flags=re.IGNORECASE)
        line = re.sub(r"<[^>]+>", "", line)
        if line.startswith("@param "):
            _, name, *description = line.split()
            line = f"**Parameter `{name}`:** {' '.join(description)}"
        elif line.startswith("@return "):
            line = f"**Returns:** {line[8:]}"
        elif line.startswith("@throws ") or line.startswith("@exception "):
            parts = line.split(maxsplit=2)
            detail = parts[2] if len(parts) > 2 else ""
            line = f"**Throws `{parts[1]}`:** {detail}"
        elif line.startswith("@"):
            line = "**" + line[1:].replace(" ", ":** ", 1)
        cleaned.append(line)
    return "\n\n".join(part for part in "\n".join(cleaned).split("\n\n") if part).strip()


def sanitize_line(line: str, in_block: bool) -> tuple[str, bool]:
    out: list[str] = []
    i = 0
    in_string = False
    quote = ""
    while i < len(line):
        if in_block:
            end = line.find("*/", i)
            if end < 0:
                return "".join(out), True
            i = end + 2
            in_block = False
            continue
        if not in_string and line.startswith("//", i):
            break
        if not in_string and line.startswith("/*", i):
            in_block = True
            i += 2
            continue
        char = line[i]
        if char in ('"', "'") and (i == 0 or line[i - 1] != "\\"):
            if in_string and char == quote:
                in_string = False
            elif not in_string:
                in_string = True
                quote = char
            out.append(" ")
        else:
            out.append(" " if in_string else char)
        i += 1
    return "".join(out), in_block


def classify(signature: str) -> str:
    core = re.sub(r"^(@\w+(?:\([^)]*\))?\s*)+", "", signature).strip()
    if re.search(r"\b(class|interface|enum|record)\b", core.split("=", 1)[0]):
        return "type"
    before_equals = core.split("=", 1)[0]
    if "(" in before_equals:
        return "callable"
    return "field"


def extract_members(source: str) -> list[Member]:
    lines = source.splitlines()
    members: list[Member] = []
    in_comment = False
    pending_doc = ""
    doc_buffer: list[str] = []
    collecting_doc = False
    collecting = False
    declaration: list[str] = []
    declaration_start = 0
    declaration_doc = ""
    parens = 0

    for number, raw in enumerate(lines, 1):
        if not collecting and "/**" in raw:
            collecting_doc = True
            doc_buffer = [raw[raw.index("/**") :]]
            if "*/" in raw[raw.index("/**") + 3 :]:
                collecting_doc = False
                pending_doc = clean_javadoc("\n".join(doc_buffer))
            continue
        if collecting_doc:
            doc_buffer.append(raw)
            if "*/" in raw:
                collecting_doc = False
                pending_doc = clean_javadoc("\n".join(doc_buffer))
            continue

        sanitized, in_comment = sanitize_line(raw, in_comment)
        stripped = sanitized.strip()
        if not collecting:
            if not stripped or stripped.startswith("@"):
                continue
            implicit_interface_method = (
                "=" not in stripped
                and re.match(
                    r"^(?:default\s+)?(?:[A-Za-z_$][\w$<>?,.\[\]]*\s+)+"
                    r"[A-Za-z_$][\w$]*\s*\([^;{}]*\)\s*;$",
                    stripped,
                )
                is not None
                and not re.match(
                    r"^(public|protected|private|static|return|throw|new|if|for|while|switch|catch|synchronized)\b",
                    stripped,
                )
            )
            if re.match(r"^(public|protected)\b", stripped) or implicit_interface_method:
                collecting = True
                declaration = [raw.strip()]
                declaration_start = number
                declaration_doc = pending_doc
                pending_doc = ""
                parens = sanitized.count("(") - sanitized.count(")")
            else:
                pending_doc = ""
                continue
        else:
            declaration.append(raw.strip())
            parens += sanitized.count("(") - sanitized.count(")")

        joined_sanitized = " ".join(declaration)
        if collecting and parens <= 0 and ("{" in joined_sanitized or ";" in joined_sanitized):
            signature = re.split(r"[;{]", joined_sanitized, maxsplit=1)[0]
            signature = re.sub(r"\s+", " ", signature).strip()
            members.append(
                Member(declaration_start, signature, classify(signature), declaration_doc)
            )
            collecting = False
            declaration = []
            parens = 0
    return members


def find_usage(class_name: str, repo: Path, sha: str) -> list[tuple[str, str]]:
    source_root = repo / "src" / "main" / "java"
    if not source_root.exists():
        return []
    pattern = re.compile(rf"\b{re.escape(class_name)}\b")
    found: list[tuple[str, str]] = []
    for java_file in sorted(source_root.rglob("*.java")):
        try:
            lines = java_file.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        line_number = next((i for i, line in enumerate(lines, 1) if pattern.search(line)), None)
        if line_number is None:
            continue
        relative = java_file.relative_to(repo).as_posix()
        url = (
            f"https://github.com/TeamSCREAMRobotics/{repo.name}/blob/"
            f"{sha}/{relative}#L{line_number}"
        )
        found.append((relative, url))
    return found[:12]


def render_member(member: Member, source_url: str) -> str:
    label = {"callable": "Callable", "field": "Exposed field", "type": "Nested/API type"}[member.kind]
    body = [f"### `{html.escape(member.signature)}`", "", f"*{label} · [source]({source_url}#L{member.line})*", ""]
    if member.docs:
        body.extend([member.docs, ""])
    elif member.kind == "callable":
        body.extend([
            "No source Javadoc is present. Use the signature and linked implementation as the contract; verify units and side effects before calling it.",
            "",
        ])
    return "\n".join(body)


def main() -> None:
    if not JAVA_ROOT.exists():
        raise SystemExit(f"SCREAMLib source not found at {JAVA_ROOT}")

    lib_sha = git_sha(LIB)
    competition_shas = {year: git_sha(repo) for year, repo in COMPETITIONS.items()}
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    index_rows: list[tuple[str, str, int, int]] = []
    total_callables = 0
    total_exposed = 0

    for java_file in sorted(JAVA_ROOT.rglob("*.java")):
        relative = java_file.relative_to(JAVA_ROOT)
        package_parts = relative.parts[:-1]
        package = ".".join(package_parts)
        class_name = java_file.stem
        source = java_file.read_text(encoding="utf-8")
        members = extract_members(source)
        callables = [member for member in members if member.kind == "callable"]
        exposed = [member for member in members if member.kind != "callable"]
        total_callables += len(callables)
        total_exposed += len(exposed)

        short_package = package.removeprefix("com.teamscreamrobotics.")
        page_dir = OUTPUT / Path(*short_package.split("."))
        page_dir.mkdir(parents=True, exist_ok=True)
        page = page_dir / f"{class_name}.md"
        repo_relative = java_file.relative_to(LIB).as_posix()
        source_url = (
            "https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/"
            f"{lib_sha}/{repo_relative}"
        )
        usage = {
            year: find_usage(class_name, repo, competition_shas[year])
            for year, repo in COMPETITIONS.items()
        }

        content = [
            f"# {class_name}",
            "",
            f"`{package}.{class_name}`",
            "",
            f"[View source]({source_url}) · **{len(callables)} callables** · **{len(exposed)} exposed fields/types**",
            "",
        ]
        if usage["2025"] or usage["2026"]:
            content.extend(["## Competition usage", ""])
            for year in ("2025", "2026"):
                if not usage[year]:
                    continue
                links = [f"[`{Path(path).name}`]({url})" for path, url in usage[year]]
                content.extend([f"**{year}:** " + ", ".join(links), ""])
        if callables:
            content.extend(["## Public and protected callables", ""])
            for member in callables:
                content.append(render_member(member, source_url))
        if exposed:
            content.extend(["## Exposed fields and types", ""])
            for member in exposed:
                content.append(render_member(member, source_url))
        page.write_text("\n".join(content).rstrip() + "\n", encoding="utf-8")
        page_relative = page.relative_to(ROOT / "docs").as_posix()
        index_rows.append((f"{short_package}.{class_name}", page_relative, len(callables), len(exposed)))

    groups: dict[str, list[tuple[str, str, int, int]]] = {}
    for row in index_rows:
        groups.setdefault(row[0].split(".", 1)[0], []).append(row)

    index = [
        "# API reference",
        "",
        f"Generated from SCREAMLib [`{lib_sha[:7]}`](https://github.com/TeamSCREAMRobotics/SCREAMLib/tree/{lib_sha}).",
        "",
        f"**{len(index_rows)} Java source files · {total_callables} public/protected callables · {total_exposed} exposed fields/types**",
        "",
        "Every signature links to its exact source line. Pages also link to matching usage in the 2025 and 2026 competition repositories.",
        "",
    ]
    for group, rows in sorted(groups.items()):
        index.extend([f"## {group}", "", "| Class | Callables | Fields/types |", "| --- | ---: | ---: |"])
        for name, page_path, callables, exposed in rows:
            relative_link = page_path.removeprefix("reference/")
            index.append(f"| [`{name}`]({relative_link}) | {callables} | {exposed} |")
        index.append("")
    (OUTPUT / "index.md").write_text("\n".join(index), encoding="utf-8")
    print(
        f"Generated {len(index_rows)} API pages with {total_callables} callables "
        f"and {total_exposed} exposed fields/types."
    )


if __name__ == "__main__":
    main()
