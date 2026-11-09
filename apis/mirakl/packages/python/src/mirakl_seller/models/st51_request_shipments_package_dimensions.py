# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class ST51RequestShipmentsPackageDimensions(ApiModel):
    """ST51RequestShipmentsPackageDimensions model."""

    height: Annotated[float, Field(le=10000, ge=0.001)]
    length: Annotated[float, Field(le=10000, ge=0.001)]
    unit: Annotated[str, Field(strict=True)]
    width: Annotated[float, Field(le=10000, ge=0.001)]
