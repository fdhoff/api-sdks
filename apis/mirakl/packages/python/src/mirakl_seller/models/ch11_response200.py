# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.ch11_response200_channels import CH11Response200Channels
from mirakl_seller._runtime import ApiModel


class CH11Response200(ApiModel):
    """CH11Response200 model."""

    channels: Optional[List[CH11Response200Channels]] = None
