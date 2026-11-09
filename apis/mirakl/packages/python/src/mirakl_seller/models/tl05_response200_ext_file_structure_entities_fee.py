# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_fee_cancelations import (
    TL05Response200ExtFileStructureEntitiesFeeCancelations,
)
from mirakl_seller.models.tl05_response200_ext_file_structure_entities_fee_refunds import (
    TL05Response200ExtFileStructureEntitiesFeeRefunds,
)
from mirakl_seller._runtime import ApiModel


class TL05Response200ExtFileStructureEntitiesFee(ApiModel):
    """TL05Response200ExtFileStructureEntitiesFee model."""

    cancelations: Optional[List[TL05Response200ExtFileStructureEntitiesFeeCancelations]] = None
    code: Optional[StrictStr] = None
    refunds: Optional[List[TL05Response200ExtFileStructureEntitiesFeeRefunds]] = None
