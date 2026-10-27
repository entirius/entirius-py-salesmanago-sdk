# AGENTS.md

SALESmanago marketing automation REST API SDK — distribution `entirius-py-salesmanago-sdk`, import `salesmanago_sdk`.

## Commands

| Command | Meaning |
|---|---|
| `make install` | sync dependencies (uv, incl. extras) |
| `make check` | lint + format-check (ruff) |
| `make fix` | auto-fix lint + format |
| `make test` | test suite (pytest) |

## Conventions

- English only: code, docs, commits, branches, PRs.
- MPL-2.0: every non-trivial source file carries the license header (pre-commit inserts it).
- Toolchain: uv + ruff + hatchling + pytest; all config in `pyproject.toml`; `uv.lock` committed.
- Git flow: `master` (production) + `develop` (integration); changes land via PR; semver tag on `master`.
- Never rename the import package `salesmanago_sdk` — it is a public API contract.
- Default: do not commit — git is the user's call.
- No AI attribution in commits or PR descriptions.

## Architecture

- `src/salesmanago_sdk/services/client.py`: `SalesmanagoClient` covers contact create/modify/delete, batch delete
  and loyalty (enroll a contact, read and modify points).
- `services/request.py`: thin HTTP wrapper over `requests`.
- `dto/`: customer, contact and loyalty payload dataclasses.
- `validators/`: response shape validation.
- `settings.py`: reads Django settings (`django.conf`) at import; tests configure a minimal Django in
  `tests/conftest.py`.
- Integration tests hit the live SALESmanago API and are skipped unless `SALESMANAGO_*` credentials are set.

## Settings

Read from Django settings in `settings.py`.

| Setting | Default | Meaning |
|---|---|---|
| `SALESMANAGO_API_URL` | `https://www.salesmanago.pl/api/` | base URL of the SALESmanago API; every request path is appended to it |
