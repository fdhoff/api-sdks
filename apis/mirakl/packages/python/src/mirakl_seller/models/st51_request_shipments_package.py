# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st51_request_shipments_package_dimensions import ST51RequestShipmentsPackageDimensions
from mirakl_seller.models.st51_request_shipments_package_weight import ST51RequestShipmentsPackageWeight
from mirakl_seller._runtime import ApiModel


class ST51RequestShipmentsPackage(ApiModel):
    """ST51RequestShipmentsPackage model."""

    dimensions: ST51RequestShipmentsPackageDimensions
    weight: ST51RequestShipmentsPackageWeight
