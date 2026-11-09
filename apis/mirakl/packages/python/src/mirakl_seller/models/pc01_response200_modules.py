# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.pc01_response200_modules_tax_manager import PC01Response200ModulesTaxManager
from mirakl_seller._runtime import ApiModel


class PC01Response200Modules(ApiModel):
    """PC01Response200Modules model."""

    mirakl_catalog_integrator: StrictBool
    mirakl_catalog_manager: StrictBool
    mirakl_catalog_transformer: StrictBool
    mirakl_platform_services: StrictBool
    offer_management: StrictBool
    offer_management_mode: Optional[StrictStr] = None
    order_management: StrictBool
    order_management_mode: Optional[StrictStr] = None
    promotions: StrictBool
    quotes: StrictBool
    tax_manager: PC01Response200ModulesTaxManager
