# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.a02_response200_updated_shop_additional_fields import (
    A02Response200UpdatedShopAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedShopAdditionalFieldsMultipleValuesList(A02Response200UpdatedShopAdditionalFields):
    """A02Response200UpdatedShopAdditionalFieldsMultipleValuesList model."""

    value: List[StrictStr]
