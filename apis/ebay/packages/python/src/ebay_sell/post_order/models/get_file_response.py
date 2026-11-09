# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_file_type import ReturnFileType
from ebay_sell._runtime import ApiModel


class GetFileResponse(ApiModel):
    """GetFileResponse model."""

    files: Optional[List[ReturnFileType]] = None
