# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0rc1] - 2026-10-26

### Added

- `SalesmanagoClient.add_contact_to_loyalty_program(loyalty_data)`: enrolls contacts in a loyalty program
  (`POST loyalty/program/v1/addContact`). Unset `LoyaltyData` fields are left out of the payload; an error status or
  a body with `success: false` raises `SalesmanagoError`.

### Changed

- Package metadata: keywords, classifiers and project URLs (docs, changelog, issues) for the PyPI page.

## [2.0.0] - 2026-07-05

Initial public release.

### Added

- `SalesmanagoClient` — customer create/modify/delete and batch delete over the SALESmanago REST API.
- DTOs for customer, contact and loyalty payloads; response validators.
- Toolchain: uv (env + lock), ruff (lint + format), hatchling (build), pytest;
  MPL-2.0 with per-file headers; pre-commit + CI (lint, test, secret-scan).
