# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesReturns(ApiModel):
    """PC01Response200FeaturesReturns model."""

    drop_ship: Optional[StrictBool] = None
    mandatory_compliance_check: StrictBool
    marketplace: Optional[StrictBool] = None
    one_creditor: Optional[StrictBool] = None
