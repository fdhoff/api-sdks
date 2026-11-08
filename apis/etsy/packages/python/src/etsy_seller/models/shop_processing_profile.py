# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopProcessingProfile(ApiModel):
    """ShopProcessingProfile model."""

    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    readiness_state_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    readiness_state: Optional[StrictStr] = None
    min_processing_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    max_processing_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    processing_days_display_label: Optional[StrictStr] = None
