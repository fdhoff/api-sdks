# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.dr11_response200_data_document_details import DR11Response200DataDocumentDetails
from mirakl_seller.models.dr11_response200_data_entities import DR11Response200DataEntities
from mirakl_seller.models.dr11_response200_data_initial_documents import DR11Response200DataInitialDocuments
from mirakl_seller.models.dr11_response200_data_issuer import DR11Response200DataIssuer
from mirakl_seller.models.dr11_response200_data_payment import DR11Response200DataPayment
from mirakl_seller.models.dr11_response200_data_payment_destination import DR11Response200DataPaymentDestination
from mirakl_seller.models.dr11_response200_data_payment_terms import DR11Response200DataPaymentTerms
from mirakl_seller.models.dr11_response200_data_recipient import DR11Response200DataRecipient
from mirakl_seller.models.dr11_response200_data_taxes import DR11Response200DataTaxes
from mirakl_seller._runtime import ApiModel


class DR11Response200Data(ApiModel):
    """DR11Response200Data model."""

    currency_iso_code: StrictStr
    date_created: datetime
    document_details: List[DR11Response200DataDocumentDetails]
    document_number: Optional[StrictStr] = None
    document_upload_date: Optional[datetime] = None
    due_date: datetime
    entities: Optional[DR11Response200DataEntities] = None
    entity_date_created: Optional[datetime] = None
    entity_id: StrictStr
    entity_type: StrictStr
    id: StrictStr
    initial_documents: Optional[List[DR11Response200DataInitialDocuments]] = None
    initial_payment_state: StrictStr
    issue_date: datetime
    issuer: DR11Response200DataIssuer
    last_updated: datetime
    payment: Optional[DR11Response200DataPayment] = None
    payment_destination: Optional[DR11Response200DataPaymentDestination] = None
    payment_terms: Optional[DR11Response200DataPaymentTerms] = None
    recipient: Optional[DR11Response200DataRecipient] = None
    state: StrictStr
    taxes: Optional[List[DR11Response200DataTaxes]] = None
    total_amount_excluding_taxes: float
    total_amount_including_taxes: float
    total_tax_amount: float
    type: StrictStr
