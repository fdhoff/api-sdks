# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class ShopListingFile(ApiModel):
    """ShopListingFile model."""

    listing_file_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    listing_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    rank: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    filename: Optional[StrictStr] = None
    filesize: Optional[StrictStr] = None
    size_bytes: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    filetype: Optional[StrictStr] = None
    create_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=946684800)]] = None
