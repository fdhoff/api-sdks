# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class P51Response200ProductImportTrackingsIntegrationDetails(ApiModel):
    """P51Response200ProductImportTrackingsIntegrationDetails model."""

    invalid_products: Optional[StrictInt] = None
    products_not_accepted_in_time: Optional[StrictInt] = None
    products_not_synchronized_in_time: Optional[StrictInt] = None
    products_reimported: Optional[StrictInt] = None
    products_successfully_synchronized: Optional[StrictInt] = None
    products_with_synchronization_issues: Optional[StrictInt] = None
    products_with_wrong_identifiers: Optional[StrictInt] = None
    rejected_products: Optional[StrictInt] = None
