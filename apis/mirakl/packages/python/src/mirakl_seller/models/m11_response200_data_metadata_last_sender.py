# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.m11_response200_data_metadata_last_sender_organization_details import (
    M11Response200DataMetadataLastSenderOrganizationDetails,
)
from mirakl_seller._runtime import ApiModel


class M11Response200DataMetadataLastSender(ApiModel):
    """M11Response200DataMetadataLastSender model."""

    display_name: StrictStr
    organization_details: Optional[M11Response200DataMetadataLastSenderOrganizationDetails] = None
    type: StrictStr
