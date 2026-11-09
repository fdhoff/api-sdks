# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p51_response200_product_import_trackings import P51Response200ProductImportTrackings
from mirakl_seller._runtime import ApiModel


class P51Response200(ApiModel):
    """P51Response200 model."""

    product_import_trackings: Optional[List[P51Response200ProductImportTrackings]] = None
    total_count: StrictInt
