# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.books_external_party_id_counterparty_id import BooksExternalPartyIdCounterpartyId
from mercury_banking.models.books_external_party_id_customer_id import BooksExternalPartyIdCustomerId
from typing import Union

BooksExternalPartyId = Union[BooksExternalPartyIdCounterpartyId, BooksExternalPartyIdCustomerId]
