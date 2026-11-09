# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pr03_request_application_to_cart import PR03RequestApplicationToCart
from mirakl_seller.models.pr03_request_public_descriptions import PR03RequestPublicDescriptions
from mirakl_seller.models.pr03_request_reward import PR03RequestReward
from mirakl_seller.models.pr03_request_trigger import PR03RequestTrigger
from mirakl_seller._runtime import ApiModel


class PR03Request(ApiModel):
    """PR03Request model."""

    application_to_cart: Optional[List[PR03RequestApplicationToCart]] = None
    channel_codes: Optional[List[StrictStr]] = None
    customer_group_ids: Optional[List[StrictStr]] = None
    customer_organization_ids: Optional[List[StrictStr]] = None
    end_date: Optional[datetime] = None
    internal_description: StrictStr
    internal_id: StrictStr
    public_descriptions: Optional[List[PR03RequestPublicDescriptions]] = None
    reward: PR03RequestReward
    start_date: datetime
    trigger: PR03RequestTrigger
