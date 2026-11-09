# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p41_request_multipart_form_data_conversion_options_ai_enrichment import (
    P41RequestMultipartFormDataConversionOptionsAiEnrichment,
)
from mirakl_seller.models.p41_request_multipart_form_data_conversion_options_ai_rewrite import (
    P41RequestMultipartFormDataConversionOptionsAiRewrite,
)
from mirakl_seller.models.p41_request_multipart_form_data_conversion_options_ai_translation import (
    P41RequestMultipartFormDataConversionOptionsAiTranslation,
)
from mirakl_seller._runtime import ApiModel


class P41RequestMultipartFormDataConversionOptions(ApiModel):
    """P41RequestMultipartFormDataConversionOptions model."""

    ai_enrichment: Optional[P41RequestMultipartFormDataConversionOptionsAiEnrichment] = None
    ai_rewrite: Optional[P41RequestMultipartFormDataConversionOptionsAiRewrite] = None
    ai_translation: Optional[P41RequestMultipartFormDataConversionOptionsAiTranslation] = None
