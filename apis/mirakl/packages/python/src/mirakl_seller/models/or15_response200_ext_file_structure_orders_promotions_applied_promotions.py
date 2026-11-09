# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_promotions_applied_promotions_campaign import (
    OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsCampaign,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_promotions_applied_promotions_configuration import (
    OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsConfiguration,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotions(ApiModel):
    """OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotions model."""

    apportioned: StrictBool
    campaign: Optional[OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsCampaign] = None
    configuration: OR15Response200ExtFileStructureOrdersPromotionsAppliedPromotionsConfiguration
    deduced_amount: float
    id: StrictStr
    offered_quantity: Optional[StrictInt] = None
    promo_code: Optional[StrictStr] = None
