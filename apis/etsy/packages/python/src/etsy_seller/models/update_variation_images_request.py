# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from etsy_seller.models.update_variation_images_request_variation_images_inner import (
    UpdateVariationImagesRequestVariationImagesInner,
)
from etsy_seller._runtime import ApiModel


class UpdateVariationImagesRequest(ApiModel):
    """UpdateVariationImagesRequest model."""

    variation_images: List[UpdateVariationImagesRequestVariationImagesInner]
