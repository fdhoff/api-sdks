# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p42_response200_conversion_options_ai_enrichment import (
    P42Response200ConversionOptionsAiEnrichment,
)
from mirakl_seller.models.p42_response200_conversion_options_ai_rewrite import P42Response200ConversionOptionsAiRewrite
from mirakl_seller.models.p42_response200_conversion_options_ai_translation import (
    P42Response200ConversionOptionsAiTranslation,
)
from mirakl_seller._runtime import ApiModel


class P42Response200ConversionOptions(ApiModel):
    """P42Response200ConversionOptions model."""

    ai_enrichment: Optional[P42Response200ConversionOptionsAiEnrichment] = None
    ai_rewrite: Optional[P42Response200ConversionOptionsAiRewrite] = None
    ai_translation: Optional[P42Response200ConversionOptionsAiTranslation] = None
