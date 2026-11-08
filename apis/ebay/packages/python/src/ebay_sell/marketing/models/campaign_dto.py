# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.campaign_audience import CampaignAudience
from ebay_sell._runtime import ApiModel


class CampaignDTO(ApiModel):
    """CampaignDTO model."""

    audiences: Optional[List[CampaignAudience]] = None
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    email_campaign_id: Optional[StrictStr] = Field(default=None, alias="emailCampaignId")
    email_campaign_status: Optional[StrictStr] = Field(default=None, alias="emailCampaignStatus")
    email_campaign_type: Optional[StrictStr] = Field(default=None, alias="emailCampaignType")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    modification_date: Optional[StrictStr] = Field(default=None, alias="modificationDate")
    schedule_date: Optional[StrictStr] = Field(default=None, alias="scheduleDate")
    schedule_date_type: Optional[StrictStr] = Field(default=None, alias="scheduleDateType")
    sent_date: Optional[StrictStr] = Field(default=None, alias="sentDate")
    subject: Optional[StrictStr] = None
