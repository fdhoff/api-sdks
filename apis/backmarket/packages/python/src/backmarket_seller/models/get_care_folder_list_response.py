# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.care_folder import CareFolder
from backmarket_seller._runtime import ApiModel


class GetCareFolderListResponse(ApiModel):
    """GetCareFolderListResponse model."""

    count: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    previous: Optional[StrictStr] = None
    results: Optional[List[CareFolder]] = None
