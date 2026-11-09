# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.m14_request_multipart_form_data_thread_input_entity import (
    M14RequestMultipartFormDataThreadInputEntity,
)
from mirakl_seller.models.m14_request_multipart_form_data_thread_input_topic import (
    M14RequestMultipartFormDataThreadInputTopic,
)
from mirakl_seller._runtime import ApiModel


class M14RequestMultipartFormDataThreadInput(ApiModel):
    """M14RequestMultipartFormDataThreadInput model."""

    body: Annotated[str, Field(min_length=3, strict=True, max_length=50000)]
    entity: M14RequestMultipartFormDataThreadInputEntity
    topic: M14RequestMultipartFormDataThreadInputTopic
