# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.gpg_key_email import GPGKeyEmail
from gitea_rest._runtime import ApiModel


class GPGKey(ApiModel):
    """GPGKey model."""

    can_certify: Optional[StrictBool] = None
    can_encrypt_comms: Optional[StrictBool] = None
    can_encrypt_storage: Optional[StrictBool] = None
    can_sign: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    emails: Optional[List[GPGKeyEmail]] = None
    expires_at: Optional[datetime] = None
    id: Optional[StrictInt] = None
    key_id: Optional[StrictStr] = None
    primary_key_id: Optional[StrictStr] = None
    public_key: Optional[StrictStr] = None
    subkeys: Optional[List[GPGKey]] = None
    verified: Optional[StrictBool] = None


GPGKey.model_rebuild(raise_errors=False)
