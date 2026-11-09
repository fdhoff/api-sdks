# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.st41_request_shipments_package import ST41RequestShipmentsPackage
from mirakl_seller._runtime import ApiModel


class ST41RequestShipments(ApiModel):
    """ST41RequestShipments model."""

    carrier_code: Optional[Annotated[str, Field(strict=True)]] = None
    carrier_service_code: Optional[Annotated[str, Field(strict=True)]] = None
    package: Optional[ST41RequestShipmentsPackage] = None
    shipment_id: StrictStr
