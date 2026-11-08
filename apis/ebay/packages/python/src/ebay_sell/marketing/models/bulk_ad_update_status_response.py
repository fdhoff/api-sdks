# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.ad_update_status_response import AdUpdateStatusResponse
from ebay_sell._runtime import ApiModel


class BulkAdUpdateStatusResponse(ApiModel):
    """BulkAdUpdateStatusResponse model."""

    responses: Optional[List[AdUpdateStatusResponse]] = None
