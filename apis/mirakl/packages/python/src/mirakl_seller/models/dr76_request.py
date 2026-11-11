# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.dr76_request_requests import DR76RequestRequests
from mirakl_seller._runtime import ApiModel


class DR76Request(ApiModel):
    """DR76Request model."""

    requests: Annotated[List[DR76RequestRequests], Field(min_length=1, max_length=100)]
