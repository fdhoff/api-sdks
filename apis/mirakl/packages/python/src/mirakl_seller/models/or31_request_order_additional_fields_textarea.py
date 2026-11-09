# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or31_request_order_additional_fields import OR31RequestOrderAdditionalFields
from mirakl_seller._runtime import ApiModel


class OR31RequestOrderAdditionalFieldsTextarea(OR31RequestOrderAdditionalFields):
    """OR31RequestOrderAdditionalFieldsTextarea model."""

    value: StrictStr
