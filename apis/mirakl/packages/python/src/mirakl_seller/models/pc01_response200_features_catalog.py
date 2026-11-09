# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesCatalog(ApiModel):
    """PC01Response200FeaturesCatalog model."""

    allow_shop_contribution_to_all_channels: StrictBool
    exclude_invalid_products: StrictBool
    list_of_multiple_values_separator: StrictStr
    product_acceptance_by_channel: StrictBool
    product_data_validation_by_channel: StrictBool
    product_import_only_on_leaf: StrictBool
