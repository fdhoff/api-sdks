# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.taxonomy_property_scale import TaxonomyPropertyScale
from etsy_seller.models.taxonomy_property_value import TaxonomyPropertyValue
from etsy_seller._runtime import ApiModel


class TaxonomyNodeProperty(ApiModel):
    """TaxonomyNodeProperty model."""

    property_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    name: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = None
    scales: Optional[List[TaxonomyPropertyScale]] = None
    is_required: Optional[StrictBool] = None
    supports_attributes: Optional[StrictBool] = None
    supports_variations: Optional[StrictBool] = None
    is_multivalued: Optional[StrictBool] = None
    max_values_allowed: Optional[StrictInt] = None
    possible_values: Optional[List[TaxonomyPropertyValue]] = None
    selected_values: Optional[List[TaxonomyPropertyValue]] = None
