# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class UpdateListingPersonalizationRequestPersonalizationQuestionsInnerOptionsInner(ApiModel):
    """UpdateListingPersonalizationRequestPersonalizationQuestionsInnerOptionsInner model."""

    option_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    label: StrictStr
