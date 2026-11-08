# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.campaign_audience import CampaignAudience
from ebay_sell._runtime import ApiModel


class GetEmailCampaignAudiencesResponse(ApiModel):
    """GetEmailCampaignAudiencesResponse model."""

    audiences: Optional[List[CampaignAudience]] = None
    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
