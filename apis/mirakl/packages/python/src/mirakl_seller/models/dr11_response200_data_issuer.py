# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_issuer_organization import DR11Response200DataIssuerOrganization
from mirakl_seller._runtime import ApiModel


class DR11Response200DataIssuer(ApiModel):
    """DR11Response200DataIssuer model."""

    id: Optional[StrictStr] = None
    locale: Optional[StrictStr] = None
    organization: DR11Response200DataIssuerOrganization
    type: StrictStr
