# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pc01_response200_features_shop_tax_options_local_tax_number import (
    PC01Response200FeaturesShopTaxOptionsLocalTaxNumber,
)
from mirakl_seller.models.pc01_response200_features_shop_tax_options_tax_identification_number import (
    PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber,
)
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesShopTaxOptions(ApiModel):
    """PC01Response200FeaturesShopTaxOptions model."""

    local_tax_number: Optional[PC01Response200FeaturesShopTaxOptionsLocalTaxNumber] = None
    tax_identification_number: PC01Response200FeaturesShopTaxOptionsTaxIdentificationNumber
