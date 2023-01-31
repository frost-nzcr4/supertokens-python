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

from typing import Union

from supertokens_python.ingredients.emaildelivery import EmailDeliveryIngredient
from supertokens_python.ingredients.emaildelivery.types import (
    EmailDeliveryInterface,
    SMTPServiceInterface,
)
from supertokens_python.recipe.emailpassword import types as ep_types
from supertokens_python.recipe.multitenancy.constants import DEFAULT_TENANT_ID

from ..thirdparty.types import ThirdPartyInfo


class User:
    def __init__(
        self,
        user_id: str,
        email: str,
        time_joined: int,
        third_party_info: Union[ThirdPartyInfo, None] = None,
    ):
        self.user_id = user_id
        self.email = email
        self.time_joined = time_joined
        self.third_party_info = third_party_info
        self.tenant_ids = [DEFAULT_TENANT_ID]

        self._update_tenant_ids()

    def _update_tenant_ids(self):
        if self.third_party_info is not None:
            if "|" in self.third_party_info.user_id:
                self.tenant_ids = [self.third_party_info.user_id.split("|")[1]]


# Export:
EmailTemplateVars = ep_types.EmailTemplateVars
PasswordResetEmailTemplateVars = ep_types.PasswordResetEmailTemplateVars

SMTPOverrideInput = SMTPServiceInterface[EmailTemplateVars]

EmailDeliveryOverrideInput = EmailDeliveryInterface[EmailTemplateVars]


class ThirdPartyEmailPasswordIngredients:
    def __init__(
        self,
        email_delivery: Union[EmailDeliveryIngredient[EmailTemplateVars], None] = None,
    ) -> None:
        self.email_delivery = email_delivery
