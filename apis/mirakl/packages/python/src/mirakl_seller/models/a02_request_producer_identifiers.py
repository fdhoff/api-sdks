# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class A02RequestProducerIdentifiers(ApiModel):
    """A02RequestProducerIdentifiers model."""

    epr_category_code: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
    producer_id: Annotated[str, Field(min_length=0, strict=True, max_length=255)]
