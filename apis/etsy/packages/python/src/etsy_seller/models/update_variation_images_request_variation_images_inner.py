# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class UpdateVariationImagesRequestVariationImagesInner(ApiModel):
    """UpdateVariationImagesRequestVariationImagesInner model."""

    property_id: Annotated[int, Field(strict=True, ge=1)]
    value_id: Annotated[int, Field(strict=True, ge=1)]
    image_id: Annotated[int, Field(strict=True, ge=1)]
