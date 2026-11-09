# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pr01_response200_promotions_application_to_cart import (
    PR01Response200PromotionsApplicationToCart,
)
from mirakl_seller.models.pr01_response200_promotions_campaign import PR01Response200PromotionsCampaign
from mirakl_seller.models.pr01_response200_promotions_channels import PR01Response200PromotionsChannels
from mirakl_seller.models.pr01_response200_promotions_medias import PR01Response200PromotionsMedias
from mirakl_seller.models.pr01_response200_promotions_public_descriptions import (
    PR01Response200PromotionsPublicDescriptions,
)
from mirakl_seller.models.pr01_response200_promotions_triggers import PR01Response200PromotionsTriggers
from mirakl_seller._runtime import ApiModel


class PR01Response200Promotions(ApiModel):
    """PR01Response200Promotions model."""

    amount_off: Optional[float] = None
    application_to_cart: List[PR01Response200PromotionsApplicationToCart]
    campaign: Optional[PR01Response200PromotionsCampaign] = None
    channels: List[PR01Response200PromotionsChannels]
    customer_group_ids: Optional[List[StrictStr]] = None
    customer_organization_ids: Optional[List[StrictStr]] = None
    date_created: datetime
    end_date: datetime
    free_items_quantity: Optional[StrictInt] = None
    internal_description: StrictStr
    internal_id: StrictStr
    last_updated: datetime
    max_quantity_to_discount: Optional[StrictInt] = None
    medias: List[PR01Response200PromotionsMedias]
    percentage_off: Optional[float] = None
    public_descriptions: List[PR01Response200PromotionsPublicDescriptions]
    reduced_unit_price: Optional[float] = None
    reward_offer_ids: Optional[List[StrictInt]] = None
    reward_on_purchased_items: StrictBool
    start_date: datetime
    state: StrictStr
    trigger_offer_ids: Optional[List[StrictInt]] = None
    triggers: List[PR01Response200PromotionsTriggers]
    type: StrictStr
