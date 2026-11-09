# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pr04_request_application_to_cart import PR04RequestApplicationToCart
from mirakl_seller.models.pr04_request_public_descriptions import PR04RequestPublicDescriptions
from mirakl_seller.models.pr04_request_reward import PR04RequestReward
from mirakl_seller.models.pr04_request_trigger import PR04RequestTrigger
from mirakl_seller._runtime import ApiModel


class PR04Request(ApiModel):
    """PR04Request model."""

    application_to_cart: Optional[List[PR04RequestApplicationToCart]] = None
    channel_codes: Optional[List[StrictStr]] = None
    customer_group_ids: Optional[List[StrictStr]] = None
    customer_organization_ids: Optional[List[StrictStr]] = None
    end_date: Optional[datetime] = None
    internal_description: StrictStr
    public_descriptions: Optional[List[PR04RequestPublicDescriptions]] = None
    reward: PR04RequestReward
    start_date: datetime
    trigger: PR04RequestTrigger
