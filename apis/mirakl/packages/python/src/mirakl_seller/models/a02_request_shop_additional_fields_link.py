# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.a02_request_shop_additional_fields import A02RequestShopAdditionalFields
from mirakl_seller._runtime import ApiModel


class A02RequestShopAdditionalFieldsLink(A02RequestShopAdditionalFields):
    """A02RequestShopAdditionalFieldsLink model."""

    value: StrictStr
