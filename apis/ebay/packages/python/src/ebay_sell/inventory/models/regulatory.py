# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.document import Document
from ebay_sell.inventory.models.energy_efficiency_label import EnergyEfficiencyLabel
from ebay_sell.inventory.models.hazmat import Hazmat
from ebay_sell.inventory.models.manufacturer import Manufacturer
from ebay_sell.inventory.models.product_safety import ProductSafety
from ebay_sell.inventory.models.responsible_person import ResponsiblePerson
from ebay_sell._runtime import ApiModel


class Regulatory(ApiModel):
    """Regulatory model."""

    documents: Optional[List[Document]] = None
    energy_efficiency_label: Optional[EnergyEfficiencyLabel] = Field(default=None, alias="energyEfficiencyLabel")
    hazmat: Optional[Hazmat] = None
    manufacturer: Optional[Manufacturer] = None
    product_safety: Optional[ProductSafety] = Field(default=None, alias="productSafety")
    repair_score: Optional[float] = Field(default=None, alias="repairScore")
    responsible_persons: Optional[List[ResponsiblePerson]] = Field(default=None, alias="responsiblePersons")
