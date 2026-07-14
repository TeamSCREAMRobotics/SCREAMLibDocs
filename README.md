# SCREAMLib Documentation

MkDocs Material documentation for [TeamSCREAMRobotics/SCREAMLib](https://github.com/TeamSCREAMRobotics/SCREAMLib), configured for Read the Docs.

## Local preview

```powershell
python -m pip install -r requirements.txt
python -m mkdocs serve
```

## Verification

```powershell
python tools/generate_api.py
python -m mkdocs build --strict
```

The API generator expects local checkouts of `SCREAMLib`, `4522_2025Competition`, and `4522_2026Competition` in the sibling `Documents/GitHub` directory. The generated Markdown is committed, so Read the Docs does not need those repositories during its build.

