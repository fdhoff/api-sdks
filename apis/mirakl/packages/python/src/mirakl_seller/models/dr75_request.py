# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.dr75_request_requests import DR75RequestRequests
from mirakl_seller._runtime import ApiModel


class DR75Request(ApiModel):
    """DR75Request model."""

    requests: Annotated[List[DR75RequestRequests], Field(min_length=1, max_length=100)]
