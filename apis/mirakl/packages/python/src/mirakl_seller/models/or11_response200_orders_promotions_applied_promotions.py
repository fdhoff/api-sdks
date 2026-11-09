# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_promotions_applied_promotions_campaign import (
    OR11Response200OrdersPromotionsAppliedPromotionsCampaign,
)
from mirakl_seller.models.or11_response200_orders_promotions_applied_promotions_configuration import (
    OR11Response200OrdersPromotionsAppliedPromotionsConfiguration,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersPromotionsAppliedPromotions(ApiModel):
    """OR11Response200OrdersPromotionsAppliedPromotions model."""

    apportioned: StrictBool
    campaign: Optional[OR11Response200OrdersPromotionsAppliedPromotionsCampaign] = None
    configuration: OR11Response200OrdersPromotionsAppliedPromotionsConfiguration
    deduced_amount: float
    id: StrictStr
    offered_quantity: Optional[StrictInt] = None
    promo_code: Optional[StrictStr] = None
