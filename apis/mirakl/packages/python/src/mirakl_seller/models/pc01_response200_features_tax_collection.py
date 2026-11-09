# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesTaxCollection(ApiModel):
    """PC01Response200FeaturesTaxCollection model."""

    activated: StrictStr
    product_tax_code_mandatory: StrictBool
    tax_collection_by_operator: StrictBool
