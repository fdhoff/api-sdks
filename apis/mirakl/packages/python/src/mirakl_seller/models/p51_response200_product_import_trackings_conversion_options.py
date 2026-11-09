# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p51_response200_product_import_trackings_conversion_options_ai_enrichment import (
    P51Response200ProductImportTrackingsConversionOptionsAiEnrichment,
)
from mirakl_seller.models.p51_response200_product_import_trackings_conversion_options_ai_rewrite import (
    P51Response200ProductImportTrackingsConversionOptionsAiRewrite,
)
from mirakl_seller.models.p51_response200_product_import_trackings_conversion_options_ai_translation import (
    P51Response200ProductImportTrackingsConversionOptionsAiTranslation,
)
from mirakl_seller._runtime import ApiModel


class P51Response200ProductImportTrackingsConversionOptions(ApiModel):
    """P51Response200ProductImportTrackingsConversionOptions model."""

    ai_enrichment: Optional[P51Response200ProductImportTrackingsConversionOptionsAiEnrichment] = None
    ai_rewrite: Optional[P51Response200ProductImportTrackingsConversionOptionsAiRewrite] = None
    ai_translation: Optional[P51Response200ProductImportTrackingsConversionOptionsAiTranslation] = None
