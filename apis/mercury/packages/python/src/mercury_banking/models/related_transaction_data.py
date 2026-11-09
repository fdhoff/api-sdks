# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.transaction_relation_kind import TransactionRelationKind
from mercury_banking._runtime import ApiModel


class RelatedTransactionData(ApiModel):
    """RelatedTransactionData model."""

    account_id: UUID = Field(alias="accountId")
    amount: Annotated[float, Field(multiple_of=0.01)]
    id: UUID
    relation_kind: TransactionRelationKind = Field(alias="relationKind")
