# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from backmarket_seller._runtime import ApiModel


class ListingsCatalog(ApiModel):
    """ListingsCatalog model."""

    catalog: Annotated[str, Field(min_length=1, strict=True)]
    quotechar: Annotated[str, Field(min_length=1, strict=True, max_length=1)]
    delimiter: Annotated[str, Field(min_length=1, strict=True, max_length=1)]
    encoding: Annotated[str, Field(min_length=2, strict=True, max_length=64)]
