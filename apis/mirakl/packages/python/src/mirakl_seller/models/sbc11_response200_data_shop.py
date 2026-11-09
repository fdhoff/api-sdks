# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class SBC11Response200DataShop(ApiModel):
    """SBC11Response200DataShop model."""

    shop_corporate_name: Optional[StrictStr] = None
    shop_id: Optional[StrictInt] = None
    shop_model: Optional[StrictStr] = None
    shop_name: Optional[StrictStr] = None
    shop_operator_internal_id: Optional[StrictStr] = None
