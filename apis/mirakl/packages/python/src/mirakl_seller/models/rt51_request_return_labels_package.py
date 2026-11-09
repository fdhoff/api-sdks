# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.rt51_request_return_labels_package_dimensions import RT51RequestReturnLabelsPackageDimensions
from mirakl_seller.models.rt51_request_return_labels_package_weight import RT51RequestReturnLabelsPackageWeight
from mirakl_seller._runtime import ApiModel


class RT51RequestReturnLabelsPackage(ApiModel):
    """RT51RequestReturnLabelsPackage model."""

    dimensions: RT51RequestReturnLabelsPackageDimensions
    weight: RT51RequestReturnLabelsPackageWeight
