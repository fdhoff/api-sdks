# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or15_response200_ext_file_structure_orders import OR15Response200ExtFileStructureOrders
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructure(ApiModel):
    """OR15Response200ExtFileStructure model."""

    orders: List[OR15Response200ExtFileStructureOrders]
