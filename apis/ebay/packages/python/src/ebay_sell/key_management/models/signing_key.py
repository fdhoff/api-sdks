# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class SigningKey(ApiModel):
    """SigningKey model."""

    creation_time: Optional[StrictInt] = Field(default=None, alias="creationTime")
    expiration_time: Optional[StrictInt] = Field(default=None, alias="expirationTime")
    jwe: Optional[StrictStr] = None
    private_key: Optional[StrictStr] = Field(default=None, alias="privateKey")
    public_key: Optional[StrictStr] = Field(default=None, alias="publicKey")
    signing_key_cipher: Optional[StrictStr] = Field(default=None, alias="signingKeyCipher")
    signing_key_id: Optional[StrictStr] = Field(default=None, alias="signingKeyId")
