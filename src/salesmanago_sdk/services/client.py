# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import logging

from salesmanago_sdk.dto.customer import BatchDeleteCustomerData, CustomerData, DeleteCustomerData
from salesmanago_sdk.dto.loyalty import LoyaltyData, ModifyPointsData
from salesmanago_sdk.exceptions import SalesmanagoError
from salesmanago_sdk.services.request import Request
from salesmanago_sdk.validators.response import validate_salesmanago_request, validate_salesmanago_response

logger_process = logging.getLogger("process")


class SalesmanagoClient:
    clientId: str
    apiKey: str
    sha: str
    owner: str

    def __init__(self, clientId: str, apiKey: str, sha: str, owner: str):
        self.clientId = clientId
        self.apiKey = apiKey
        self.sha = sha
        self.owner = owner

    def create_or_modify_customer(self, customer_data: CustomerData):
        request = Request(method="POST", resource="contact/upsert", auth=self, data=customer_data.asdict())
        response = request.make_request()
        validation, response_body = validate_salesmanago_response(response, request)
        if validation:
            success = validate_salesmanago_request(response_body)
            if success:
                return response_body
            else:
                logger_process.error(
                    "Salesmanago API response failed",
                    extra={"details": {"request_params": request.params, "response_body": response_body}},
                )
                raise SalesmanagoError("Salesmanago response is not correct.")
        else:
            raise SalesmanagoError(
                f"The salesmanago API responded with an error. Message: {response_body.get('message')}"
            )

    def delete_customer(self, delete_customer_data: DeleteCustomerData):
        request = Request(method="POST", resource="contact/delete", auth=self, data=delete_customer_data.asdict())
        response = request.make_request()
        validation, response_body = validate_salesmanago_response(response, request)
        if validation:
            success = validate_salesmanago_request(response_body)
            if success:
                return response_body
            else:
                logger_process.error(
                    "Salesmanago API response failed",
                    extra={"details": {"request_params": request.params, "response_body": response_body}},
                )
                raise SalesmanagoError("Salesmanago response is not correct.")
        else:
            raise SalesmanagoError(
                f"The salesmanago API responded with an error. Message: {response_body.get('message')}"
            )

    def batch_delete_customer(self, batch_delete_customer_data: BatchDeleteCustomerData):
        request = Request(
            method="POST", resource="contact/batchDelete", auth=self, data=batch_delete_customer_data.to_dict()
        )
        response = request.make_request()
        validation, response_body = validate_salesmanago_response(response, request)
        if validation:
            success = validate_salesmanago_request(response_body)
            if success:
                return response_body
            else:
                logger_process.error(
                    "Salesmanago API response failed",
                    extra={"details": {"request_params": request.params, "response_body": response_body}},
                )
                raise SalesmanagoError("Salesmanago response is not correct.")
        else:
            raise SalesmanagoError(
                f"The salesmanago API responded with an error. Message: {response_body.get('message')}"
            )

    def get_loyalty_points(self, loyalty_data: LoyaltyData):
        request = Request(method="GET", resource="loyalty/program/v1/getPoints", auth=self, data=loyalty_data.asdict())
        response = request.make_request()
        validation, response_body = validate_salesmanago_response(response, request)
        if validation:
            success = validate_salesmanago_request(response_body)
            if success:
                return response_body
            else:
                logger_process.error(
                    "Salesmanago API response failed",
                    extra={"details": {"request_params": request.params, "response_body": response_body}},
                )
                raise SalesmanagoError("Salesmanago response is not correct.")
        else:
            raise SalesmanagoError(
                f"The salesmanago API responded with an error. Message: {response_body.get('message')}"
            )

    def add_contact_to_loyalty_program(self, loyalty_data: LoyaltyData):
        request = Request(
            method="POST", resource="loyalty/program/v1/addContact", auth=self, data=loyalty_data.to_dict()
        )
        response = request.make_request()
        validation, response_body = validate_salesmanago_response(response, request)
        if validation:
            success = validate_salesmanago_request(response_body)
            if success:
                return response_body
            else:
                logger_process.error(
                    "Salesmanago API response failed",
                    extra={"details": {"request_params": request.params, "response_body": response_body}},
                )
                raise SalesmanagoError("Salesmanago response is not correct.")
        else:
            raise SalesmanagoError(
                f"The salesmanago API responded with an error. Message: {response_body.get('message')}"
            )

    def modify_loyalty_points(self, modify_points_data: ModifyPointsData):
        request = Request(
            method="POST", resource="loyalty/program/v1/modifyPoints", auth=self, data=modify_points_data.asdict()
        )
        response = request.make_request()
        validation, response_body = validate_salesmanago_response(response, request)
        if validation:
            success = validate_salesmanago_request(response_body)
            if success:
                return response_body
            else:
                logger_process.error(
                    "Salesmanago API response failed",
                    extra={"details": {"request_params": request.params, "response_body": response_body}},
                )
                raise SalesmanagoError("Salesmanago response is not correct.")
        else:
            raise SalesmanagoError(
                f"The salesmanago API responded with an error. Message: {response_body.get('message')}"
            )
