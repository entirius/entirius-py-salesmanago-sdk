# entirius-py-salesmanago-sdk

A Python client for the SALESmanago marketing automation REST API, part of Entirius, the open-source modular ecommerce platform.
It creates, modifies and deletes contacts and enrolls contacts in a loyalty program and reads and changes their points behind one `SalesmanagoClient` class.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-salesmanago-sdk.svg)](https://pypi.org/project/entirius-py-salesmanago-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-salesmanago-sdk.svg)](https://pypi.org/project/entirius-py-salesmanago-sdk/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-salesmanago-sdk/blob/develop/LICENSE)

## What it does

- Creates or modifies a contact from a typed `CustomerData` DTO (`create_or_modify_customer()`).
- Deletes one contact or a batch of contacts (`delete_customer()`, `batch_delete_customer()`).
- Enrolls a contact in a loyalty program (`add_contact_to_loyalty_program()`), reads and modifies its points
  (`get_loyalty_points()`, `modify_loyalty_points()`).
- Raises `SalesmanagoError` when the API answers with an error or an unexpected body.

## Installation

```shell
uv add entirius-py-salesmanago-sdk
pip install entirius-py-salesmanago-sdk
```

The import name is `salesmanago_sdk`.

The SDK reads one Django setting, `SALESMANAGO_API_URL` (default `https://www.salesmanago.pl/api/`); set it in the
project settings to target another endpoint. It is not a Django app: no `INSTALLED_APPS` entry is needed.

## Quick start

```python
from salesmanago_sdk.dto.customer import CustomerContact, CustomerData
from salesmanago_sdk.services.client import SalesmanagoClient

client = SalesmanagoClient(clientId="...", apiKey="...", sha="...", owner="...")
client.create_or_modify_customer(
    customer_data=CustomerData(contact=CustomerContact(email="user@example.com")),
)
```

## Requirements

- Python 3.11 or newer.
- Django 4.2 or newer, with settings configured before the package is imported.
- `requests` and `marshmallow` (installed as dependencies).
- A SALESmanago account (client id, API key, SHA, owner).

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-salesmanago-sdk/blob/develop/CHANGELOG.md

## Part of Entirius

This SDK is one of the marketing integration clients used by the Entirius backend service (Volkanos).

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Sibling marketing SDKs: https://github.com/entirius/entirius-py-edrone-sdk, https://github.com/entirius/entirius-py-get-response-sdk, https://github.com/entirius/entirius-py-synerise-sdk

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest); integration tests are skipped without SALESMANAGO_* credentials
```

Development and agent instructions: https://github.com/entirius/entirius-py-salesmanago-sdk/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-salesmanago-sdk/blob/develop/LICENSE.
