# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.update_negative_keyword_id_request import UpdateNegativeKeywordIdRequest
from ebay_sell._runtime import ApiModel


class BulkUpdateNegativeKeywordRequest(ApiModel):
    """BulkUpdateNegativeKeywordRequest model."""

    requests: Optional[List[UpdateNegativeKeywordIdRequest]] = None
