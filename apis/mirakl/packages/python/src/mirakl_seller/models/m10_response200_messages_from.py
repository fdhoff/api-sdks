# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m10_response200_messages_from_organization_details import (
    M10Response200MessagesFromOrganizationDetails,
)
from mirakl_seller._runtime import ApiModel


class M10Response200MessagesFrom(ApiModel):
    """M10Response200MessagesFrom model."""

    display_name: StrictStr
    organization_details: Optional[M10Response200MessagesFromOrganizationDetails] = None
    type: StrictStr
