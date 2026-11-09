# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class DR12Response200DataFeesDebitOneOffReferences(ApiModel):
    """DR12Response200DataFeesDebitOneOffReferences model."""

    type: Annotated[str, Field(min_length=1, strict=True, max_length=100)]
    value: Annotated[str, Field(min_length=1, strict=True, max_length=100)]
