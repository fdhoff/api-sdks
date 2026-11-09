# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st41_request_shipments_package_dimensions import ST41RequestShipmentsPackageDimensions
from mirakl_seller.models.st41_request_shipments_package_weight import ST41RequestShipmentsPackageWeight
from mirakl_seller._runtime import ApiModel


class ST41RequestShipmentsPackage(ApiModel):
    """ST41RequestShipmentsPackage model."""

    dimensions: ST41RequestShipmentsPackageDimensions
    weight: ST41RequestShipmentsPackageWeight
