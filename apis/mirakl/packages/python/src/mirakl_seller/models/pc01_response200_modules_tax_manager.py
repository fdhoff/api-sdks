# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.pc01_response200_modules_tax_manager_tax_provider import (
    PC01Response200ModulesTaxManagerTaxProvider,
)
from mirakl_seller._runtime import ApiModel


class PC01Response200ModulesTaxManager(ApiModel):
    """PC01Response200ModulesTaxManager model."""

    activated: StrictBool
    tax_provider: PC01Response200ModulesTaxManagerTaxProvider
