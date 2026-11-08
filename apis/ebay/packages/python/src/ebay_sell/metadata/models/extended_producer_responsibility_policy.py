# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.extended_producer_responsibility import ExtendedProducerResponsibility
from ebay_sell._runtime import ApiModel


class ExtendedProducerResponsibilityPolicy(ApiModel):
    """ExtendedProducerResponsibilityPolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    supported_attributes: Optional[List[ExtendedProducerResponsibility]] = Field(
        default=None, alias="supportedAttributes"
    )
