# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller._runtime import ApiModel


class Issue(ApiModel):
    """Issue model."""

    customer_issue: Optional[StrictStr] = Field(default=None, alias="customerIssue")
    tag: Optional[StrictStr] = None
