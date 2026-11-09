# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR43RequestMultipartFormDataThreadInputTopicReasonCode(ApiModel):
    """OR43RequestMultipartFormDataThreadInputTopicReasonCode model."""

    type: StrictStr
    value: Annotated[str, Field(min_length=1, strict=True, max_length=200)]
