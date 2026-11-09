# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedPaymentInfo(ApiModel):
    """A02Response200UpdatedPaymentInfo model."""

    type: Optional[StrictStr] = Field(default=None, alias="@type")
    owner: Annotated[str, Field(min_length=1, strict=True, max_length=100)]
