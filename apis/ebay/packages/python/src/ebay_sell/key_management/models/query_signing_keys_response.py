# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.key_management.models.signing_key import SigningKey
from ebay_sell._runtime import ApiModel


class QuerySigningKeysResponse(ApiModel):
    """QuerySigningKeysResponse model."""

    signing_keys: Optional[List[SigningKey]] = Field(default=None, alias="signingKeys")
