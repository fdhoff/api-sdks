# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt51_request_return_labels_label_options import RT51RequestReturnLabelsLabelOptions
from mirakl_seller.models.rt51_request_return_labels_package import RT51RequestReturnLabelsPackage
from mirakl_seller.models.rt51_request_return_labels_shipping_from import RT51RequestReturnLabelsShippingFrom
from mirakl_seller._runtime import ApiModel


class RT51RequestReturnLabels(ApiModel):
    """RT51RequestReturnLabels model."""

    carrier_code: Optional[StrictStr] = None
    carrier_service_code: Optional[StrictStr] = None
    label_options: Optional[RT51RequestReturnLabelsLabelOptions] = None
    label_selection_mode: Optional[StrictStr] = None
    package: RT51RequestReturnLabelsPackage
    return_id: StrictStr
    shipping_from: Optional[RT51RequestReturnLabelsShippingFrom] = None
