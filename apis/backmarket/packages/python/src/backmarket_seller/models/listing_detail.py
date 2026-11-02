# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from backmarket_seller.models.aesthetic_grade_value import AestheticGradeValue
from backmarket_seller.models.listing_public_shippings_inner import ListingPublicShippingsInner
from backmarket_seller.models.listing_state_value import ListingStateValue
from backmarket_seller._runtime import ApiModel


class ListingDetail(ApiModel):
    """ListingDetail model."""

    backmarket_id: StrictInt
    comment: Optional[StrictStr]
    currency: StrictStr
    id: UUID
    listing_id: StrictInt
    max_price: StrictStr
    min_price: Optional[StrictStr]
    price: StrictStr
    product_id: UUID
    publication_state: StrictInt
    quantity: StrictInt
    shippings: List[ListingPublicShippingsInner]
    sku: StrictStr
    state: ListingStateValue
    grade: AestheticGradeValue
    title: StrictStr
    warranty_delay: StrictInt
    new_battery: Optional[StrictBool] = False
    outlet: Optional[StrictBool] = False
    statuscode: StrictInt
