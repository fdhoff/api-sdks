# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.dr76_response200_requests import DR76Response200Requests
from mirakl_seller._runtime import ApiModel


class DR76Response200(ApiModel):
    """DR76Response200 model."""

    requests: List[DR76Response200Requests]
