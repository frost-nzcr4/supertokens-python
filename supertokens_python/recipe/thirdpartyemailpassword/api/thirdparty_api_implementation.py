# Copyright (c) 2021, VRAI Labs and/or its affiliates. All rights reserved.
#
# This software is licensed under the Apache License, Version 2.0 (the
# "License") as published by the Apache Software Foundation.
#
# You may not use this file except in compliance with the License. You may
# obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from typing import Any, Dict, Union

from supertokens_python.recipe.thirdparty.interfaces import (
    APIInterface, APIOptions)
from supertokens_python.recipe.thirdparty.provider import Provider
from supertokens_python.recipe.thirdpartyemailpassword.interfaces import \
    APIInterface as ThirdPartyEmailPasswordAPIInterface


def get_interface_impl(
        api_implementation: ThirdPartyEmailPasswordAPIInterface) -> APIInterface:
    implementation = APIInterface()

    implementation.disable_authorisation_url_get = api_implementation.disable_authorisation_url_get
    implementation.disable_sign_in_up_post = api_implementation.disable_thirdparty_sign_in_up_post
    implementation.disable_apple_redirect_handler_post = api_implementation.disable_apple_redirect_handler_post

    if not implementation.disable_sign_in_up_post:
        async def sign_in_up_post(provider: Provider, code: str, redirect_uri: str, client_id: Union[str, None], auth_code_response: Union[Dict[str, Any], None], api_options: APIOptions, user_context: Dict[str, Any]):
            return await api_implementation.thirdparty_sign_in_up_post(provider, code, redirect_uri, client_id, auth_code_response, api_options, user_context)

        implementation.sign_in_up_post = sign_in_up_post

    implementation.authorisation_url_get = api_implementation.authorisation_url_get
    implementation.apple_redirect_handler_post = api_implementation.apple_redirect_handler_post

    return implementation
