# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from backmarket_seller._runtime import ApiModel


class MonetaryAmount(ApiModel):
    """MonetaryAmount model."""

    amount: Annotated[str, Field(strict=True)]
    currency: Annotated[str, Field(strict=True)]
