# Maintaining these docs

The API pages are generated from the checked-out SCREAMLib source so the signature inventory, implementation analysis, and inline competition examples stay complete.

## Regenerate the reference

Place these repositories beside this documentation repository under `Documents/GitHub`:

- `SCREAMLib`
- `4522_2025Competition`
- `4522_2026Competition`

Then run:

```powershell
python tools/generate_api.py
python -m mkdocs build --strict
```

The generator replaces only `docs/reference`. Curated guides and examples remain hand-maintained.

## Update checklist

1. Update the SCREAMLib version and snapshot links in `docs/index.md` and `docs/getting-started.md`.
2. Regenerate the API catalog.
3. Add or refresh examples when a competition robot adopts a new class.
4. Run the strict MkDocs build.
5. Let Read the Docs build from `.readthedocs.yaml`.
