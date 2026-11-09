# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a02_response200_errors import A02Response200Errors
from mirakl_seller.models.a02_response200_updated import A02Response200Updated
from mirakl_seller._runtime import ApiModel


class A02Response200(ApiModel):
    """A02Response200 model."""

    errors: Optional[List[A02Response200Errors]] = None
    updated: Optional[A02Response200Updated] = None
