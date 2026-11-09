# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.vl11_response200_values_lists_label_translations import (
    VL11Response200ValuesListsLabelTranslations,
)
from mirakl_seller.models.vl11_response200_values_lists_values import VL11Response200ValuesListsValues
from mirakl_seller._runtime import ApiModel


class VL11Response200ValuesLists(ApiModel):
    """VL11Response200ValuesLists model."""

    code: StrictStr
    label: Optional[StrictStr] = None
    label_translations: List[VL11Response200ValuesListsLabelTranslations]
    values: Optional[List[VL11Response200ValuesListsValues]] = None
