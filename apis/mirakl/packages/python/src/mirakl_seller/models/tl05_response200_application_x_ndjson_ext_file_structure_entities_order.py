# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_order_payment_info import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderPaymentInfo,
)
from mirakl_seller.models.tl05_response200_application_x_ndjson_ext_file_structure_entities_order_references import (
    TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderReferences,
)
from mirakl_seller._runtime import ApiModel


class TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrder(ApiModel):
    """TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrder model."""

    commercial_id: Optional[StrictStr] = None
    creation_date: Optional[datetime] = None
    id: Optional[StrictStr] = None
    payment_info: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderPaymentInfo] = None
    references: Optional[TL05Response200ApplicationXNdjsonExtFileStructureEntitiesOrderReferences] = None
