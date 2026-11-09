# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.m14_request_multipart_form_data_thread_input_topic import (
    M14RequestMultipartFormDataThreadInputTopic,
)
from mirakl_seller._runtime import ApiModel


class M14RequestMultipartFormDataThreadInputTopicFreeText(M14RequestMultipartFormDataThreadInputTopic):
    """M14RequestMultipartFormDataThreadInputTopicFreeText model."""

    value: Annotated[str, Field(min_length=3, strict=True, max_length=200)]
