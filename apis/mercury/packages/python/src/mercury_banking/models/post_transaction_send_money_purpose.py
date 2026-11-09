# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.simple_purpose import SimplePurpose
from mercury_banking._runtime import ApiModel


class PostTransactionSendMoneyPurpose(ApiModel):
    """PostTransactionSendMoneyPurpose model."""

    simple: Optional[SimplePurpose] = None
