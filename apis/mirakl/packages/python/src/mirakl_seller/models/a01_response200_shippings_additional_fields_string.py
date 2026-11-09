# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.a01_response200_shippings_additional_fields import A01Response200ShippingsAdditionalFields
from mirakl_seller._runtime import ApiModel


class A01Response200ShippingsAdditionalFieldsString(A01Response200ShippingsAdditionalFields):
    """A01Response200ShippingsAdditionalFieldsString model."""

    value: StrictStr
