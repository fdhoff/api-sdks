# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller._runtime import ApiModel


class SellerTaxonomyNode(ApiModel):
    """SellerTaxonomyNode model."""

    id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    level: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    name: Optional[StrictStr] = None
    parent_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    children: Optional[List[SellerTaxonomyNode]] = None
    full_path_taxonomy_ids: Optional[List[Annotated[int, Field(strict=True, ge=1)]]] = None


SellerTaxonomyNode.model_rebuild(raise_errors=False)
