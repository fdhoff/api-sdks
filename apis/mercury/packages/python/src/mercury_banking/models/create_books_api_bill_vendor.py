# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.create_books_api_bill_vendor_counterparty_id import CreateBooksAPIBillVendorCounterpartyId
from mercury_banking.models.create_books_api_bill_vendor_recipient_id import CreateBooksAPIBillVendorRecipientId
from typing import Union

CreateBooksAPIBillVendor = Union[CreateBooksAPIBillVendorCounterpartyId, CreateBooksAPIBillVendorRecipientId]
