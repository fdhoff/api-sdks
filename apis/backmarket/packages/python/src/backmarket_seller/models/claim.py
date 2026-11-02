# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.issue import Issue
from backmarket_seller.models.return_label import ReturnLabel
from backmarket_seller.models.tile import Tile
from backmarket_seller._runtime import ApiModel


class Claim(ApiModel):
    """Claim model."""

    id: Optional[StrictInt] = None
    tiles: Optional[List[Tile]] = None
    issues: Optional[List[Issue]] = None
    rate: Optional[StrictInt] = None
    score: Optional[StrictInt] = None
    state: Optional[StrictInt] = None
    withdraw: Optional[StrictBool] = None
    gras_savoye: Optional[StrictBool] = None
    warnings: Optional[List[Any]] = None
    resolution_choice: Optional[StrictStr] = None
    declared_warranty_state: Optional[StrictStr] = None
    return_labels: Optional[List[ReturnLabel]] = None
