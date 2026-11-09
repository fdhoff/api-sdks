# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.credit_account_statement_payload import CreditAccountStatementPayload
from mercury_banking.models.depository_account_statement_payload import DepositoryAccountStatementPayload
from typing import Union

AccountStatementPayloadAccountDetails = Union[DepositoryAccountStatementPayload, CreditAccountStatementPayload]
