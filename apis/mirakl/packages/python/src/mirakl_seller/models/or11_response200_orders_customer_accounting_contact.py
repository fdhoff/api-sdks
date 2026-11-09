# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersCustomerAccountingContact(ApiModel):
    """OR11Response200OrdersCustomerAccountingContact model."""

    civility: Optional[Annotated[str, Field(strict=True, max_length=20)]] = None
    customer_id: Annotated[str, Field(strict=True, max_length=50)]
    firstname: Annotated[str, Field(strict=True, max_length=255)]
    lastname: Annotated[str, Field(strict=True, max_length=255)]
    locale: Optional[StrictStr] = None
