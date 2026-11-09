# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class A02Response200UpdatedSpecificBillingInformationsFiscalInformation(ApiModel):
    """A02Response200UpdatedSpecificBillingInformationsFiscalInformation model."""

    local_tax_number: Optional[StrictStr] = None
    tax_identification_country: Optional[StrictStr] = None
    tax_identification_number: Optional[StrictStr] = None
