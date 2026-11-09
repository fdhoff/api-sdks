# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_invoice_details_document_details import (
    OR11Response200OrdersInvoiceDetailsDocumentDetails,
)
from mirakl_seller.models.or11_response200_orders_invoice_details_payment_terms import (
    OR11Response200OrdersInvoiceDetailsPaymentTerms,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersInvoiceDetails(ApiModel):
    """OR11Response200OrdersInvoiceDetails model."""

    document_details: Optional[List[OR11Response200OrdersInvoiceDetailsDocumentDetails]] = None
    payment_terms: Optional[OR11Response200OrdersInvoiceDetailsPaymentTerms] = None
