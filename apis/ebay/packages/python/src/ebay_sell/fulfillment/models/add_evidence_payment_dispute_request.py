# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.file_evidence import FileEvidence
from ebay_sell.fulfillment.models.order_line_items import OrderLineItems
from ebay_sell._runtime import ApiModel


class AddEvidencePaymentDisputeRequest(ApiModel):
    """AddEvidencePaymentDisputeRequest model."""

    evidence_type: Optional[StrictStr] = Field(default=None, alias="evidenceType")
    files: Optional[List[FileEvidence]] = None
    line_items: Optional[List[OrderLineItems]] = Field(default=None, alias="lineItems")
