# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR11Response200DataIssuerOrganizationPersonalInformation(ApiModel):
    """DR11Response200DataIssuerOrganizationPersonalInformation model."""

    civility: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
