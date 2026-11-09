# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A01Response200ApplicableTaxes(ApiModel):
    """A01Response200ApplicableTaxes model."""

    code: StrictStr
    fee_types: Optional[List[StrictStr]] = None
    label: StrictStr
