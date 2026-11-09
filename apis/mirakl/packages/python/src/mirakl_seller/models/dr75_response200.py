# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.dr75_response200_requests import DR75Response200Requests
from mirakl_seller._runtime import ApiModel


class DR75Response200(ApiModel):
    """DR75Response200 model."""

    requests: List[DR75Response200Requests]
