# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.m12_request_multipart_form_data_message_input_to import (
    M12RequestMultipartFormDataMessageInputTo,
)
from mirakl_seller.models.m12_request_multipart_form_data_message_input_topic import (
    M12RequestMultipartFormDataMessageInputTopic,
)
from mirakl_seller._runtime import ApiModel


class M12RequestMultipartFormDataMessageInput(ApiModel):
    """M12RequestMultipartFormDataMessageInput model."""

    body: Annotated[str, Field(min_length=3, strict=True, max_length=50000)]
    to: List[M12RequestMultipartFormDataMessageInputTo]
    topic: Optional[M12RequestMultipartFormDataMessageInputTopic] = None
