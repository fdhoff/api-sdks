# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersEcoContributions(ApiModel):
    """OF21Response200OffersEcoContributions model."""

    eco_contribution_amount: Optional[float] = None
    epr_category_code: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    producer_id: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
