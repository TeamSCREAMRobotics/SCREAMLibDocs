"""Generate implementation-derived MkDocs API pages for SCREAMLib.

The generator treats Java source as the authority. JavaDoc is retained only as a
secondary author note; behavior, side effects, branches, calls, and examples are
derived from method bodies and competition call sites.
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import textwrap
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

CURATED_EXAMPLES: dict[str, list[tuple[str, str, int, int, str]]] = {
    "TalonFXSubsystem": [
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java",
            20,
            48,
            "Configure a TalonFX mechanism, PID slot, limits, and Motion Magic",
        ),
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/hood/Hood.java",
            1,
            50,
            "Create a mechanism by subclassing TalonFXSubsystem",
        ),
        (
            "2025",
            "src/main/java/frc2025/subsystems/superstructure/elevator/Elevator.java",
            16,
            73,
            "Model semantic goals and apply them as commands (legacy package names)",
        ),
    ],
    "ScreamPIDConstants": [
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java",
            40,
            55,
            "Build a Phoenix slot with PID and feedforward gains",
        ),
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/hood/HoodConstants.java",
            30,
            47,
            "Configure position gains and Motion Magic values",
        ),
    ],
    "LimelightHelpers": [
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/vision/VisionManager.java",
            134,
            183,
            "Set robot orientation, select MegaTag mode, reject estimates, and add odometry data",
        )
    ],
    "LimelightVision": [
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/vision/VisionManager.java",
            35,
            64,
            "Declare named Limelights and their robot-relative poses",
        )
    ],
    "Length": [
        (
            "2025",
            "src/main/java/frc2025/constants/FieldConstants.java",
            51,
            93,
            "Keep field dimensions and zone sizes unit-safe (legacy package names)",
        ),
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/flywheel/FlywheelConstants.java",
            12,
            21,
            "Represent wheel dimensions and derived circumference",
        ),
    ],
    "AllianceFlipUtil": [
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/Shooter.java",
            260,
            330,
            "Select alliance-correct shooting and ferry targets",
        ),
        (
            "2025",
            "src/main/java/frc2025/RobotContainer.java",
            190,
            228,
            "Select alliance-specific headings and poses (legacy package names)",
        ),
    ],
    "RunnableUtil": [
        (
            "2025",
            "src/main/java/frc2025/Robot.java",
            25,
            77,
            "Reload an autonomous command only when the dashboard selection changes",
        )
    ],
    "GeomUtil": [
        (
            "2026",
            "src/main/java/frc2026/tars/subsystems/shooter/Shooter.java",
            490,
            505,
            "Compose robot, turret, hood, and shooter transforms",
        ),
        (
            "2025",
            "src/main/java/frc2025/commands/AutoAlign.java",
            195,
            229,
            "Convert translations into transforms while calculating an alignment setpoint",
        ),
    ],
}

CLASS_GUIDES: dict[str, str] = {
    "TalonFXSubsystem": """## How to use this subsystem base

`TalonFXSubsystem` owns one master TalonFX, optional followers, cached Phoenix status signals, control-request objects, configuration, goal state, telemetry, and simulation state. A mechanism subclass normally does **not** reimplement the motor loop. It supplies configuration and calls the appropriate setpoint method.

### 1. Build the configuration before construction

Create one `TalonFXSubsystemConfiguration` in the mechanism constants class. At minimum, set `name` and `masterConstants`. Then choose the mechanism ratio, neutral mode, current limits, PID slots, soft limits, Motion Magic values, and simulation constants that apply to that mechanism.

- `sensorToMechRatio` converts rotor sensor units into mechanism units.
- `rotorToSensorRatio` is used when a remote/feedback sensor has a separate ratio.
- `minUnitsLimit` and `maxUnitsLimit` become software limits when enabled.
- `slot0`, `slot1`, and `slot2` are Phoenix gains, commonly built through `ScreamPIDConstants`.
- `cruiseVelocity`, `acceleration`, and `jerk` configure Motion Magic.
- `codeEnabled`, `logTelemetry`, and `debugMode` control whether requests run and how much is logged.

The constructor copies these values into a `TalonFXConfiguration`, applies it to the master/followers, creates cached status signals, builds reusable control request objects, and registers simulation when configured. Configuration therefore needs to be complete **before** `super(config)` runs.

### 2. Choose one control path

| Intent | Method | Units/behavior |
| --- | --- | --- |
| Open-loop percent | `setDutyCycle(...)` | Duty cycle, normally `-1.0` to `1.0`, plus optional duty-cycle feedforward. |
| Direct voltage | `setVoltage(...)` | Volts, plus optional voltage feedforward. |
| Closed-loop position | `setSetpointPosition(...)` | Mechanism units after the configured sensor/mechanism ratios. |
| Motion Magic position | `setSetpointMotionMagicPosition(...)` | Mechanism units, using configured cruise velocity/acceleration/jerk. |
| Closed-loop velocity | `setSetpointVelocity(...)` | Mechanism units per second. |
| Motion Magic velocity | `setSetpointMotionMagicVelocity(...)` | Velocity target using Motion Magic velocity shaping. |
| Arbitrary Phoenix request | `setMaster(...)` / `applyControlCommand(...)` | Passes the supplied CTRE `ControlRequest` through directly. |

Each setpoint method updates the library's cached `setpoint`, marks whether velocity mode is active, fills the matching reusable CTRE request, and sends it through `setMaster`. `setMaster` is the final gate: it respects emergency-stop/code-enabled state before writing to hardware.

### 3. Use goals when the mechanism has named states

Implement `TalonFXSubsystemGoal` as an enum. `target()` supplies the live target, `controlType()` selects the request type, and `feedForward()` can supply a changing feedforward. `applyGoal(...)` switches on the goal's control type and dispatches to the corresponding setter. `applyGoalCommand(...)` wraps that work in a WPILib command for bindings and command groups.

### 4. Read state and determine completion

`getPosition()` and `getVelocity()` return mechanism-side values; rotor-specific accessors return rotor-side values. `getError()` subtracts measured position/velocity from the cached setpoint according to the current mode. `atGoal()` uses the configuration tolerance, while `atGoal(absTolerance)` lets the caller override it.

### 5. Safety, runtime reconfiguration, and simulation

- `stop()` sends a neutral request. `stopAll(...)` applies it to multiple SCREAMLib mechanisms.
- `emergencyStop()` latches the subsystem's emergency-stop flag and stops output; inspect `isActive()` before assuming later requests are accepted.
- Checked configuration mutators route Phoenix status through `ErrorChecker`; `Unchecked` variants skip that reporting and should be used only when the caller handles failure.
- `periodic()` refreshes cached signals, applies the active goal, and emits telemetry when enabled.
- `simulationPeriodic()` advances the configured `SimWrapper`; `setSimState(...)` pushes simulated position/velocity back to the subsystem and registered callback.

!!! warning "Units are configuration-dependent"
    Position and velocity setters use the mechanism units implied by the configured feedback ratios. Simulation backends also use different native units (for example meters for an elevator and rotations for a DC motor). Read the individual method's implementation notes below before mixing rotor, sensor, mechanism, or simulation values.
""",
    "Logger": """## How logging dispatch works

`Logger` is a static overload layer over DogLog. Each `log(...)` overload converts or forwards one supported WPILib/Java value type to DogLog under the supplied key. Geometry arrays are flattened through `DataConversions`; structured objects such as trajectories and swerve states are converted to the numeric representation expected by dashboards and log readers. Timed overloads rate-limit publication through a per-key timestamp map. Review the exact overload below because array shape and unit representation differ by type.
""",
    "LimelightHelpers": """## How to use this generated helper safely

`LimelightHelpers` is a broad NetworkTables adapter. Getter families read named Limelight entries and convert raw doubles/arrays/JSON into typed target, pose, and estimate objects. Setter families publish camera pose, crop, priority-tag, pipeline, orientation, and Python data back to NetworkTables. Pose-estimate methods also compensate timestamps with reported latency. The implementation details below show the exact NetworkTables key for every call; use those details when diagnosing an empty/default result.

!!! note "Default values are meaningful"
    Many getters return `0`, an empty array/string, or an empty result when an entry is missing. A default value is not proof that a valid target was observed; pair pose/target reads with the relevant validity and tag-count checks.
""",
}


@dataclass
class Member:
    line: int
    end_line: int
    signature: str
    kind: str
    docs: str
    code: str = ""
    body: str = ""
    generated: bool = False


@dataclass
class UsageExample:
    year: str
    path: str
    start: int
    end: int
    title: str
    code: str
    url: str


def git_sha(repo: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True
    ).strip()


def clean_javadoc(block: str) -> str:
    lines = block.splitlines()
    cleaned: list[str] = []
    for line in lines:
        line = re.sub(r"^\s*/?\*+/?\s?", "", line)
        line = re.sub(r"\s*\*/\s*$", "", line).strip()
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
    return "\n\n".join(
        part for part in "\n".join(cleaned).split("\n\n") if part
    ).strip()


def sanitize_line(line: str, in_block: bool) -> tuple[str, bool]:
    """Remove comments and string contents while preserving braces and layout."""
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
    if "(" in core.split("=", 1)[0]:
        return "callable"
    return "field"


def attach_implementation(member: Member, lines: list[str]) -> None:
    """Attach the complete declaration/body and ending source line."""
    start = member.line - 1
    in_comment = False
    started_body = False
    depth = 0
    end = start
    for index in range(start, len(lines)):
        sanitized, in_comment = sanitize_line(lines[index], in_comment)
        if not started_body:
            brace = sanitized.find("{")
            semicolon = sanitized.find(";")
            if semicolon >= 0 and (brace < 0 or semicolon < brace):
                end = index
                break
            if brace >= 0:
                started_body = True
                depth = sanitized[brace:].count("{") - sanitized[brace:].count("}")
                if depth == 0:
                    end = index
                    break
        else:
            depth += sanitized.count("{") - sanitized.count("}")
            if depth == 0:
                end = index
                break
        end = index

    member.end_line = end + 1
    member.code = textwrap.dedent("\n".join(lines[start : end + 1])).strip()
    if started_body and "{" in member.code:
        body = member.code.split("{", 1)[1]
        if body.rfind("}") >= 0:
            body = body[: body.rfind("}")]
        member.body = body.strip()


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
                and (
                    re.match(
                        r"^(?:[A-Za-z_$][\w$<>?,.\[\]]*\s+)+"
                        r"[A-Za-z_$][\w$]*\s*\([^;{}]*\)\s*;$",
                        stripped,
                    )
                    is not None
                    or re.match(
                        r"^default\s+(?:[A-Za-z_$][\w$<>?,.\[\]]*\s+)+"
                        r"[A-Za-z_$][\w$]*\s*\([^;{}]*\)\s*\{$",
                        stripped,
                    )
                    is not None
                )
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

        joined = " ".join(declaration)
        if collecting and parens <= 0 and ("{" in joined or ";" in joined):
            signature = re.split(r"[;{]", joined, maxsplit=1)[0]
            signature = re.sub(r"\s+", " ", signature).strip()
            member = Member(
                declaration_start,
                declaration_start,
                signature,
                classify(signature),
                declaration_doc,
            )
            attach_implementation(member, lines)
            members.append(member)
            collecting = False
            declaration = []
            parens = 0
    return members


def add_record_callables(members: list[Member]) -> None:
    """Document canonical constructors and accessors generated by Java records."""
    existing = {member.signature for member in members if member.kind == "callable"}
    additions: list[Member] = []
    for record in [member for member in members if member.kind == "type" and re.search(r"\brecord\b", member.signature)]:
        match = re.search(r"\brecord\s+([A-Za-z_$][\w$]*)(?:<[^>]+>)?\s*\((.*)\)\s*$", record.signature)
        if not match:
            continue
        record_name, raw_components = match.groups()
        components = split_parameters(f"record({raw_components})")
        canonical = f"public {record_name}({raw_components})"
        if canonical not in existing:
            additions.append(
                Member(
                    record.line,
                    record.line,
                    canonical,
                    "callable",
                    "Java generates this canonical constructor from the record header.",
                    record.signature,
                    "",
                    True,
                )
            )
        for java_type, name in components:
            accessor = f"public {java_type} {name}()"
            if accessor in existing:
                continue
            additions.append(
                Member(
                    record.line,
                    record.line,
                    accessor,
                    "callable",
                    f"Java generates this accessor for the `{name}` record component.",
                    record.signature,
                    "",
                    True,
                )
            )
    members.extend(additions)


def split_parameters(signature: str) -> list[tuple[str, str]]:
    if "(" not in signature or ")" not in signature:
        return []
    raw = signature[signature.find("(") + 1 : signature.rfind(")")].strip()
    if not raw:
        return []
    chunks: list[str] = []
    current: list[str] = []
    angle = square = round_depth = 0
    for char in raw:
        angle += 1 if char == "<" else -1 if char == ">" else 0
        square += 1 if char == "[" else -1 if char == "]" else 0
        round_depth += 1 if char == "(" else -1 if char == ")" else 0
        if char == "," and angle == square == round_depth == 0:
            chunks.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    chunks.append("".join(current).strip())
    parameters: list[tuple[str, str]] = []
    for chunk in chunks:
        chunk = re.sub(r"@\w+(?:\([^)]*\))?\s*", "", chunk)
        chunk = re.sub(r"\bfinal\s+", "", chunk).strip()
        parts = chunk.rsplit(" ", 1)
        if len(parts) == 2:
            parameters.append((parts[0].strip(), parts[1].strip()))
    return parameters


def method_name(signature: str) -> str:
    before = signature[: signature.find("(")] if "(" in signature else signature
    match = re.search(r"([A-Za-z_$][\w$]*)\s*$", before)
    return match.group(1) if match else "callable"


def return_type(signature: str, class_name: str) -> str | None:
    name = method_name(signature)
    if name == class_name:
        return None
    before = signature[: signature.find("(")]
    before = re.sub(r"@\w+(?:\([^)]*\))?\s*", "", before)
    before = re.sub(
        r"\b(public|protected|static|final|synchronized|abstract|default|native|strictfp)\b",
        "",
        before,
    )
    tokens = before.split()
    # A declaration with only the callable name is a constructor, including
    # constructors of public nested classes/records on a containing-class page.
    if len(tokens) == 1:
        return None
    return " ".join(tokens[:-1])


def compact(expression: str, limit: int = 180) -> str:
    value = re.sub(r"\s+", " ", expression).strip()
    return value if len(value) <= limit else value[: limit - 1] + "…"


def parameter_detail(name: str, java_type: str, docs: str) -> str:
    documented = re.search(
        rf"\*\*Parameter `{re.escape(name)}`:\*\*\s*(.*?)(?=\n\n\*\*|$)",
        docs,
        re.DOTALL,
    )
    if documented and documented.group(1).strip():
        return compact(documented.group(1), 220)
    lower = name.lower()
    unit_rules = [
        (("volt", "voltage"), "Voltage value in volts."),
        (("radian",), "Angular value in radians."),
        (("degree",), "Angular value in degrees."),
        (("meter",), "Linear value in meters."),
        (("inch",), "Linear value in inches."),
        (("second", "deltatime", "period"), "Time value in seconds."),
        (("rotation",), "Mechanism or rotor rotations; verify the configured ratio."),
        (("rpm",), "Rotational speed in revolutions per minute."),
        (("rps",), "Rotational speed in revolutions per second."),
        (("velocity", "speed"), "Velocity/speed in the units required by this API and configuration."),
        (("position",), "Position in the units required by this API and configuration."),
        (("enable",), "Enables the behavior when `true`; disables it when `false`."),
        (("supplier",), "Evaluated when the operation runs, so it may provide a changing value."),
        (("tolerance", "epsilon"), "Allowed absolute error around the target."),
    ]
    for needles, description in unit_rules:
        if any(needle in lower for needle in needles):
            return description
    if java_type.endswith("Supplier") or "Supplier<" in java_type:
        return "Callback evaluated at use time rather than construction time."
    return f"`{java_type}` input consumed by the implementation shown below."


def exposed_field_names(members: list[Member]) -> set[str]:
    names: set[str] = set()
    for member in members:
        if member.kind != "field":
            continue
        before_equals = member.signature.split("=", 1)[0]
        candidates = re.findall(r"[A-Za-z_$][\w$]*", before_equals)
        if candidates:
            names.add(candidates[-1])
    return names


def implementation_facts(member: Member, field_names: set[str]) -> list[str]:
    if member.generated:
        if "accessor" in member.docs.lower():
            return ["Java generates this record-component accessor. It returns the immutable component value captured by the record's canonical constructor."]
        return ["Java generates this record canonical constructor. It stores each argument in the corresponding final record component; Java also supplies component accessors, value-based `equals`, `hashCode`, and `toString`."]
    if not member.body:
        return [
            "This is a declaration-only contract. The implementing class or lambda supplies the behavior; this file performs no work by itself."
        ]

    body = member.body
    clean_lines: list[str] = []
    in_comment = False
    for line in body.splitlines():
        cleaned, in_comment = sanitize_line(line, in_comment)
        clean_lines.append(cleaned)
    clean = "\n".join(clean_lines)
    name = method_name(member.signature)
    facts: list[str] = []

    returns = [compact(value) for value in re.findall(r"\breturn\s+(.+?);", body, re.DOTALL)]
    conditions = [compact(value) for value in re.findall(r"\bif\s*\((.*?)\)\s*\{?", clean, re.DOTALL)]
    throws = re.findall(r"\bthrow\s+new\s+([A-Za-z_$][\w$.]*)\s*\(", clean)
    calls = re.findall(r"\b((?:[A-Za-z_$][\w$]*\.)*[A-Za-z_$][\w$]*)\s*\(", clean)
    ignored = {
        "if", "for", "while", "switch", "catch", "return", "throw", "new", "super", "this", name,
    }
    unique_calls: list[str] = []
    for call in calls:
        leaf = call.split(".")[-1]
        if leaf in ignored or call in unique_calls:
            continue
        unique_calls.append(call)

    writes = set(re.findall(r"\b(?:this|super)\.([A-Za-z_$][\w$]*)\s*(?:=|\+=|-=|\*=|/=|\+\+|--)", clean))
    for field in field_names:
        if re.search(rf"(?<![.\w]){re.escape(field)}\s*(?:=|\+=|-=|\*=|/=|\+\+|--)", clean):
            writes.add(field)

    line_count = len([line for line in body.splitlines() if line.strip()])
    facts.append(f"The implementation executes {line_count} non-blank source line{'s' if line_count != 1 else ''}.")

    constructor_delegate = re.search(r"^\s*(this|super)\s*\((.*?)\)\s*;", body, re.DOTALL)
    if constructor_delegate:
        target = "another constructor in the same type" if constructor_delegate.group(1) == "this" else "the superclass constructor"
        facts.append(f"It delegates initialization to {target} with `{compact(constructor_delegate.group(2))}`.")

    if writes:
        facts.append("It changes object/subclass state through " + ", ".join(f"`{field}`" for field in sorted(writes)) + ".")
    if "getConfigurator().apply" in body or ".getConfigurator()" in body:
        facts.append("It interacts with a Phoenix device configurator; this can perform CAN configuration I/O and report vendor status codes.")
    if ".setControl(" in body or "setMaster(" in body:
        facts.append("It issues a CTRE control request to the master motor; calling it can immediately change actuator output.")
    if "Logger.log(" in body or "DogLog." in body:
        keys = re.findall(r"Logger\.log\(\s*([^,\n]+)", body)
        suffix = " Keys/expressions include " + ", ".join(f"`{compact(key, 60)}`" for key in keys[:4]) + "." if keys else ""
        facts.append("It publishes telemetry/log data." + suffix)
    if "NetworkTable" in body or "getEntry(" in body or ".setDouble(" in body or ".setDoubleArray(" in body:
        facts.append("It reads or writes NetworkTables data, so the result depends on live robot/network state.")
    if "DriverStation" in body or "RobotBase" in body or "RobotController" in body:
        facts.append("It reads WPILib runtime/Driver Station state; behavior may differ by alliance, enable state, real hardware, or simulation.")
    if "MathUtil.clamp" in body or "Math.max" in body or "Math.min" in body:
        facts.append("It bounds at least one intermediate or output value before use.")
    if any(token in body for token in ("Units.", "Conversions.", "fromMeters", "fromInches", "getMeters", "getInches")):
        facts.append("It performs an explicit unit or mechanism conversion; do not bypass that conversion with an unlabelled scalar.")
    if conditions:
        rendered = "; ".join(f"`{condition}`" for condition in conditions[:3])
        extra = f" plus {len(conditions) - 3} more" if len(conditions) > 3 else ""
        facts.append(f"It has {len(conditions)} conditional path{'s' if len(conditions) != 1 else ''}: {rendered}{extra}.")
    loop_count = len(re.findall(r"\b(for|while)\s*\(", clean))
    if loop_count:
        facts.append(f"It iterates through {loop_count} loop{'s' if loop_count != 1 else ''}; work scales with the associated collection/range.")
    if throws:
        facts.append("It can explicitly throw " + ", ".join(f"`{item}`" for item in sorted(set(throws))) + ".")
    if returns:
        shown = "; ".join(f"`{value}`" for value in returns[:3])
        extra = f"; plus {len(returns) - 3} additional return paths" if len(returns) > 3 else ""
        facts.append(f"Return path{'s' if len(returns) != 1 else ''}: {shown}{extra}.")
    if unique_calls:
        facts.append("Key collaborators/calls: " + ", ".join(f"`{call}()`" for call in unique_calls[:10]) + ".")
    return facts


def render_implementation(member: Member) -> str:
    if not member.code:
        return ""
    source_range = f"{member.line}–{member.end_line}" if member.end_line != member.line else str(member.line)
    indented = "\n".join("    " + line for line in member.code.splitlines())
    title = "Record declaration that generates this callable" if member.generated else f"Implementation (source lines {source_range})"
    return "\n".join(
        [
            f'??? example "{title}"',
            "",
            "    ```java",
            indented,
            "    ```",
            "",
        ]
    )


def render_callable(member: Member, source_url: str, class_name: str, field_names: set[str]) -> str:
    name = method_name(member.signature)
    result_type = return_type(member.signature, class_name)
    params = split_parameters(member.signature)
    body = [
        f"### `{html.escape(member.signature)}`",
        "",
        f"[Source lines {member.line}–{member.end_line}]({source_url}#L{member.line})",
        "",
        "**Detailed behavior**",
        "",
    ]
    for fact in implementation_facts(member, field_names):
        body.append(f"- {fact}")
    body.append("")

    if params:
        body.extend(["**Inputs**", "", "| Parameter | Type | Meaning |", "| --- | --- | --- |"])
        for java_type, param_name in params:
            body.append(
                f"| `{param_name}` | `{html.escape(java_type)}` | {parameter_detail(param_name, java_type, member.docs)} |"
            )
        body.append("")
    else:
        body.extend(["**Inputs:** None.", ""])

    if result_type is None:
        body.extend([f"**Result:** Constructs and initializes a `{name}` instance.", ""])
    elif result_type == "void":
        body.extend(["**Result:** No return value; observable behavior comes from the state changes and calls listed above.", ""])
    else:
        body.extend([f"**Result:** Returns `{html.escape(result_type)}`. Exact return expressions are listed in the behavior section.", ""])

    body.append(render_implementation(member))
    if member.docs:
        indented_docs = "\n".join("    " + line for line in member.docs.splitlines())
        body.extend(['??? note "Author note from JavaDoc"', "", indented_docs, ""])
    return "\n".join(body)


def render_exposed(member: Member, source_url: str, source: str) -> str:
    label = "Nested/API type" if member.kind == "type" else "Exposed field"
    body = [
        f"### `{html.escape(member.signature)}`",
        "",
        f"*{label} · [source]({source_url}#L{member.line})*",
        "",
    ]
    if member.kind == "field":
        modifiers = []
        for modifier in ("static", "final", "protected", "public"):
            if re.search(rf"\b{modifier}\b", member.signature):
                modifiers.append(modifier)
        mutable = "not reassigned after initialization" if "final" in modifiers else "mutable by callers/subclasses"
        initialized = " with an initializer" if "=" in member.signature else " without an inline initializer"
        name_match = re.findall(r"[A-Za-z_$][\w$]*", member.signature.split("=", 1)[0])
        name = name_match[-1] if name_match else "field"
        references = len(re.findall(rf"\b{re.escape(name)}\b", source))
        body.extend([
            f"This is a **{' '.join(modifiers) if modifiers else 'exposed'}** field{initialized}. It is {mutable}. The declaring source references it {references} time{'s' if references != 1 else ''}, so changing it can affect every control path that reads `{name}`.",
            "",
        ])
    else:
        type_kind = next((kind for kind in ("record", "interface", "enum", "class") if re.search(rf"\b{kind}\b", member.signature)), "type")
        body.extend([
            f"This exposed `{type_kind}` is part of the API surface. Its callable members are documented above on this page; inspect the linked declaration before adding implementations or enum values because callers may switch on the existing shape.",
            "",
        ])
    if member.docs:
        indented_docs = "\n".join("    " + line for line in member.docs.splitlines())
        body.extend(['??? note "Author note from JavaDoc"', "", indented_docs, ""])
    return "\n".join(body)


def github_url(repo: Path, sha: str, path: str, start: int, end: int | None = None) -> str:
    suffix = f"#L{start}" + (f"-L{end}" if end and end != start else "")
    return f"https://github.com/TeamSCREAMRobotics/{repo.name}/blob/{sha}/{path}{suffix}"


def make_example(year: str, path: str, start: int, end: int, title: str, sha: str) -> UsageExample | None:
    repo = COMPETITIONS[year]
    file_path = repo / Path(path)
    if not file_path.exists():
        return None
    lines = file_path.read_text(encoding="utf-8").splitlines()
    start = max(1, start)
    end = min(len(lines), end)
    code = textwrap.dedent("\n".join(lines[start - 1 : end])).strip()
    return UsageExample(year, path, start, end, title, code, github_url(repo, sha, path, start, end))


def find_examples(class_name: str, competition_shas: dict[str, str]) -> list[UsageExample]:
    curated: list[UsageExample] = []
    for year, path, start, end, title in CURATED_EXAMPLES.get(class_name, []):
        example = make_example(year, path, start, end, title, competition_shas[year])
        if example:
            curated.append(example)
    if curated:
        return curated

    pattern = re.compile(rf"\b{re.escape(class_name)}\b")
    examples: list[UsageExample] = []
    for year, repo in COMPETITIONS.items():
        source_root = repo / "src" / "main" / "java"
        candidates: list[tuple[int, Path, int]] = []
        for java_file in sorted(source_root.rglob("*.java")):
            lines = java_file.read_text(encoding="utf-8", errors="replace").splitlines()
            for index, line in enumerate(lines, 1):
                stripped = line.strip()
                if not pattern.search(line) or stripped.startswith("import ") or stripped.startswith("//"):
                    continue
                score = 0
                if f"extends {class_name}" in line or f"implements {class_name}" in line:
                    score += 6
                if f"new {class_name}" in line:
                    score += 5
                if f"{class_name}." in line:
                    score += 4
                if "class " in line or "enum " in line:
                    score += 2
                candidates.append((score, java_file, index))
        seen_files: set[Path] = set()
        for _, java_file, line_number in sorted(candidates, key=lambda item: (-item[0], str(item[1]), item[2])):
            if java_file in seen_files:
                continue
            seen_files.add(java_file)
            relative = java_file.relative_to(repo).as_posix()
            lines = java_file.read_text(encoding="utf-8", errors="replace").splitlines()
            start = max(1, line_number - 5)
            end = min(len(lines), line_number + 10)
            example = make_example(
                year,
                relative,
                start,
                end,
                f"Use `{class_name}` in `{java_file.name}`",
                competition_shas[year],
            )
            if example:
                examples.append(example)
            if len([item for item in examples if item.year == year]) >= 2:
                break
    return examples


def render_examples(examples: list[UsageExample]) -> str:
    if not examples:
        return "\n".join([
            "## Competition examples",
            "",
            "No direct reference to this class was found in the pinned 2025 or 2026 competition source. The callable sections below therefore document behavior from SCREAMLib itself instead of presenting a fabricated robot example.",
            "",
        ])
    body = ["## Competition examples", "", "These are real call sites from the pinned competition repositories, shown here so usage is available without leaving this API page.", ""]
    for example in examples:
        body.extend([
            f"### {example.year}: {example.title}",
            "",
            f"[`{example.path}` lines {example.start}–{example.end}]({example.url})",
            "",
            "```java",
            example.code,
            "```",
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

    index_rows: list[tuple[str, str, int, int, int]] = []
    total_callables = total_exposed = total_examples = 0

    for java_file in sorted(JAVA_ROOT.rglob("*.java")):
        relative = java_file.relative_to(JAVA_ROOT)
        package = ".".join(relative.parts[:-1])
        class_name = java_file.stem
        source = java_file.read_text(encoding="utf-8")
        members = extract_members(source)
        add_record_callables(members)
        callables = [member for member in members if member.kind == "callable"]
        exposed = [member for member in members if member.kind != "callable"]
        fields = exposed_field_names(members)
        examples = find_examples(class_name, competition_shas)
        total_callables += len(callables)
        total_exposed += len(exposed)
        total_examples += len(examples)

        short_package = package.removeprefix("com.teamscreamrobotics.")
        page_dir = OUTPUT / Path(*short_package.split("."))
        page_dir.mkdir(parents=True, exist_ok=True)
        page = page_dir / f"{class_name}.md"
        repo_relative = java_file.relative_to(LIB).as_posix()
        source_url = f"https://github.com/TeamSCREAMRobotics/SCREAMLib/blob/{lib_sha}/{repo_relative}"

        content = [
            f"# {class_name}",
            "",
            f"`{package}.{class_name}`",
            "",
            f"[View source]({source_url}) · **{len(callables)} callables** · **{len(exposed)} exposed fields/types** · **{len(examples)} embedded competition examples**",
            "",
            "[Jump to examples](#competition-examples){ .md-button .md-button--primary }",
            "",
        ]
        if class_name in CLASS_GUIDES:
            content.extend([CLASS_GUIDES[class_name], ""])
        content.append(render_examples(examples))
        if callables:
            content.extend(["## Public and protected callables", ""])
            for member in callables:
                content.append(render_callable(member, source_url, class_name, fields))
        if exposed:
            content.extend(["## Exposed fields and types", ""])
            for member in exposed:
                content.append(render_exposed(member, source_url, source))
        page.write_text("\n".join(content).rstrip() + "\n", encoding="utf-8")
        page_relative = page.relative_to(ROOT / "docs").as_posix()
        index_rows.append((f"{short_package}.{class_name}", page_relative, len(callables), len(exposed), len(examples)))

    groups: dict[str, list[tuple[str, str, int, int, int]]] = {}
    for row in index_rows:
        groups.setdefault(row[0].split(".", 1)[0], []).append(row)

    index = [
        "# API reference",
        "",
        f"Generated from SCREAMLib [`{lib_sha[:7]}`](https://github.com/TeamSCREAMRobotics/SCREAMLib/tree/{lib_sha}).",
        "",
        f"**{len(index_rows)} Java source files · {total_callables} public/protected callables · {total_exposed} exposed fields/types · {total_examples} embedded competition examples**",
        "",
        "This reference is implementation-derived. Every callable includes its actual source body, control-flow/state/collaborator analysis, input and result details, and exact source lines. JavaDoc appears only as a secondary author note.",
        "",
    ]
    for group, rows in sorted(groups.items()):
        index.extend([f"## {group}", "", "| Class | Callables | Fields/types | Examples |", "| --- | ---: | ---: | ---: |"])
        for name, page_path, callables, exposed, examples in rows:
            relative_link = page_path.removeprefix("reference/")
            index.append(f"| [`{name}`]({relative_link}) | {callables} | {exposed} | {examples} |")
        index.append("")
    (OUTPUT / "index.md").write_text("\n".join(index), encoding="utf-8")
    print(
        f"Generated {len(index_rows)} API pages with {total_callables} callables, "
        f"{total_exposed} exposed fields/types, and {total_examples} embedded examples."
    )


if __name__ == "__main__":
    main()
