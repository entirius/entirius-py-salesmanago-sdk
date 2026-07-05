# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
import logging

from requests import Response

logger_process = logging.getLogger("process")


def log_when_fail(response_body, request, code):
    logger_process.error(
        "The salesmanago API responded with an error",
        extra={"details": {"request_params": request.params, "response_body": response_body, "code": code}},
    )


def validate_salesmanago_response(response: Response, request) -> (bool, dict):
    response_body = json.loads(response.text)

    if response.status_code == 200:
        return True, response_body

    if response.status_code == 201:
        return True, response_body

    if response.status_code == 302:
        return True, response_body

    if response.status_code == 400:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 400)
            raise ValueError(error_message)

    if response.status_code == 401:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 401)
            raise ConnectionError(error_message)

    if response.status_code == 403:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 403)
            raise PermissionError(error_message)

    if response.status_code == 404:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 404)
            raise ValueError(error_message)

    if response.status_code == 408:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 408)
            raise TimeoutError(error_message)

    if response.status_code == 500:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 500)
            raise SystemError(error_message)

    if response.status_code == 503:
        validation, error_message = validate_salesmanago_response_body_when_error(response_body)
        if validation:
            log_when_fail(response_body, request, 503)
            raise BrokenPipeError(error_message)

    return False, response_body


def validate_salesmanago_response_body_when_error(response_body: dict) -> (bool, str):
    if "message" in response_body:
        return True, f"{response_body['message']}"
    else:
        return False, ""


def validate_salesmanago_request(response_body: dict) -> (bool, list):
    success = response_body.get("success", False)
    if success:
        return True
    else:
        return False
