# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_invoice_details_document_details import (
    OR15Response200ExtFileStructureOrdersInvoiceDetailsDocumentDetails,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_invoice_details_payment_terms import (
    OR15Response200ExtFileStructureOrdersInvoiceDetailsPaymentTerms,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersInvoiceDetails(ApiModel):
    """OR15Response200ExtFileStructureOrdersInvoiceDetails model."""

    document_details: Optional[List[OR15Response200ExtFileStructureOrdersInvoiceDetailsDocumentDetails]] = None
    payment_terms: Optional[OR15Response200ExtFileStructureOrdersInvoiceDetailsPaymentTerms] = None
