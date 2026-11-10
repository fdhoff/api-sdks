# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.payload_user import PayloadUser
from gitea_rest._runtime import ApiModel


class PayloadCommitVerification(ApiModel):
    """PayloadCommitVerification model."""

    payload: Optional[StrictStr] = None
    reason: Optional[StrictStr] = None
    signature: Optional[StrictStr] = None
    signer: Optional[PayloadUser] = None
    verified: Optional[StrictBool] = None
