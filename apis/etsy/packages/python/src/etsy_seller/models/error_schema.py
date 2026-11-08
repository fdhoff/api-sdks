# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from etsy_seller._runtime import ApiModel


class ErrorSchema(ApiModel):
    """ErrorSchema model."""

    error: StrictStr
