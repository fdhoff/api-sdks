# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.a01_response200_shop_additional_fields import A01Response200ShopAdditionalFields
from mirakl_seller._runtime import ApiModel


class A01Response200ShopAdditionalFieldsBoolean(A01Response200ShopAdditionalFields):
    """A01Response200ShopAdditionalFieldsBoolean model."""

    value: StrictStr
