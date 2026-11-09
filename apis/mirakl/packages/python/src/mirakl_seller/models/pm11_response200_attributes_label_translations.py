# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PM11Response200AttributesLabelTranslations(ApiModel):
    """PM11Response200AttributesLabelTranslations model."""

    locale: StrictStr
    value: StrictStr
