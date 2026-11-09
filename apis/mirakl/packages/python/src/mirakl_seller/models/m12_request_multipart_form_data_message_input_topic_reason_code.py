# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.m12_request_multipart_form_data_message_input_topic import (
    M12RequestMultipartFormDataMessageInputTopic,
)
from mirakl_seller._runtime import ApiModel


class M12RequestMultipartFormDataMessageInputTopicReasonCode(M12RequestMultipartFormDataMessageInputTopic):
    """M12RequestMultipartFormDataMessageInputTopicReasonCode model."""

    value: Annotated[str, Field(min_length=1, strict=True, max_length=200)]
