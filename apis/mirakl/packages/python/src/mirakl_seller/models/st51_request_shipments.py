# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.st51_request_shipments_package import ST51RequestShipmentsPackage
from mirakl_seller._runtime import ApiModel


class ST51RequestShipments(ApiModel):
    """ST51RequestShipments model."""

    carrier_code: Optional[Annotated[str, Field(strict=True)]] = None
    carrier_service_code: Optional[Annotated[str, Field(strict=True)]] = None
    label_selection_mode: Optional[StrictStr] = None
    package: Optional[ST51RequestShipmentsPackage] = None
    shipment_id: StrictStr
