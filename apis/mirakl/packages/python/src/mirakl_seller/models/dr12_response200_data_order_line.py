# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.dr12_response200_data_order_line_additional_fields import (
    DR12Response200DataOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class DR12Response200DataOrderLine(ApiModel):
    """DR12Response200DataOrderLine model."""

    additional_fields: Optional[Annotated[List[DR12Response200DataOrderLineAdditionalFields], Field(min_length=0)]] = (
        None
    )
    id: StrictStr
