# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class BuyerTaxonomyPropertyValue(ApiModel):
    """BuyerTaxonomyPropertyValue model."""

    value_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    name: Optional[StrictStr] = None
    scale_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    equal_to: Optional[List[Annotated[int, Field(strict=True, ge=0)]]] = None
