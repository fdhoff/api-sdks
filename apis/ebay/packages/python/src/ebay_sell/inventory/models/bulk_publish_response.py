# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.offer_response_with_listing_id import OfferResponseWithListingId
from ebay_sell._runtime import ApiModel


class BulkPublishResponse(ApiModel):
    """BulkPublishResponse model."""

    responses: Optional[List[OfferResponseWithListingId]] = None
