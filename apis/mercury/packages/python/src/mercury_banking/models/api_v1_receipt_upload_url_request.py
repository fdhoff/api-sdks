# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class ApiV1ReceiptUploadUrlRequest(ApiModel):
    """ApiV1ReceiptUploadUrlRequest model."""

    file_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="fileName")
