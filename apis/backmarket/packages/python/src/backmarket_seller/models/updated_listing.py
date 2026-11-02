# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from backmarket_seller.models.aesthetic_grade_value import AestheticGradeValue
from backmarket_seller.models.listing_state_value import ListingStateValue
from backmarket_seller.models.update_ws_specific_listing200_response_shippings_inner import (
    UpdateWsSpecificListing200ResponseShippingsInner,
)
from backmarket_seller._runtime import ApiModel


class UpdatedListing(ApiModel):
    """UpdatedListing model."""

    id: UUID
    listing_id: StrictInt
    product_id: Optional[UUID] = None
    backmarket_id: StrictInt
    title: StrictStr
    shippings: List[UpdateWsSpecificListing200ResponseShippingsInner]
    state: ListingStateValue
    grade: AestheticGradeValue
    quantity: StrictInt
    currency: StrictStr
    sku: StrictStr
    publication_state: StrictInt
    warranty_delay: StrictInt
    price: StrictStr
    comment: Optional[StrictStr]
    max_price: StrictStr
    shippings_response: Optional[List[StrictStr]] = None
    statuscode: StrictInt
    min_price: Optional[StrictStr]
