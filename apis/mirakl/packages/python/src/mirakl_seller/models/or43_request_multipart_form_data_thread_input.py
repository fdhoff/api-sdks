# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or43_request_multipart_form_data_thread_input_topic import (
    OR43RequestMultipartFormDataThreadInputTopic,
)
from mirakl_seller._runtime import ApiModel


class OR43RequestMultipartFormDataThreadInput(ApiModel):
    """OR43RequestMultipartFormDataThreadInput model."""

    body: Annotated[str, Field(min_length=3, strict=True, max_length=50000)]
    to: List[StrictStr]
    topic: OR43RequestMultipartFormDataThreadInputTopic
