# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from backmarket_seller.models.buyback_message_payload_files_inner import BuybackMessagePayloadFilesInner
from backmarket_seller._runtime import ApiModel


class BuybackMessagePayload(ApiModel):
    """BuybackMessagePayload model."""

    message: Annotated[str, Field(min_length=1, strict=True)]
    files: List[BuybackMessagePayloadFilesInner]
