# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class ApiV1MarkReimbursementPaidRequest(ApiModel):
    """ApiV1MarkReimbursementPaidRequest model."""

    note: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=5000)]] = None
