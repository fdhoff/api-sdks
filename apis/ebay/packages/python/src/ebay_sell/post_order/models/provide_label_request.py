# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.label_action_enum import LabelActionEnum
from ebay_sell.post_order.models.no_seller_upload_label_reason_enum import NoSellerUploadLabelReasonEnum
from ebay_sell.post_order.models.text import Text
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ProvideLabelRequest(ApiModel):
    """ProvideLabelRequest model."""

    carrier_enum: Optional[StrictStr] = Field(default=None, alias="carrierEnum")
    carrier_name: Optional[StrictStr] = Field(default=None, alias="carrierName")
    comments: Optional[Text] = None
    file_id: Optional[StrictStr] = Field(default=None, alias="fileId")
    forward_shipping_label_provided: Optional[StrictBool] = Field(default=None, alias="forwardShippingLabelProvided")
    label_action: Optional[LabelActionEnum] = Field(default=None, alias="labelAction")
    label_sent_date: Optional[Timestamp] = Field(default=None, alias="labelSentDate")
    no_label_reason: Optional[NoSellerUploadLabelReasonEnum] = Field(default=None, alias="noLabelReason")
    return_label_cost: Optional[Amount] = Field(default=None, alias="returnLabelCost")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
