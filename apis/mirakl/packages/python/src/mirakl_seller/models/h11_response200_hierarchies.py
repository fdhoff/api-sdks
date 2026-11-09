# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.h11_response200_hierarchies_label_translations import (
    H11Response200HierarchiesLabelTranslations,
)
from mirakl_seller._runtime import ApiModel


class H11Response200Hierarchies(ApiModel):
    """H11Response200Hierarchies model."""

    code: StrictStr
    label: Optional[StrictStr] = None
    label_translations: List[H11Response200HierarchiesLabelTranslations]
    level: StrictInt
    parent_code: StrictStr
