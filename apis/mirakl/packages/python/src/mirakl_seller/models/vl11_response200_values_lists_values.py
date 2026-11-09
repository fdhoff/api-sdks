# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.vl11_response200_values_lists_values_label_translations import (
    VL11Response200ValuesListsValuesLabelTranslations,
)
from mirakl_seller._runtime import ApiModel


class VL11Response200ValuesListsValues(ApiModel):
    """VL11Response200ValuesListsValues model."""

    code: StrictStr
    label: Optional[StrictStr] = None
    label_translations: List[VL11Response200ValuesListsValuesLabelTranslations]
