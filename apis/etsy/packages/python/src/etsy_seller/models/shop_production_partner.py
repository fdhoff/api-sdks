# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopProductionPartner(ApiModel):
    """ShopProductionPartner model."""

    production_partner_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    partner_name: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
