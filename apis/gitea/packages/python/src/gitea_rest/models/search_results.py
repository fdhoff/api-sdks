# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.repository import Repository
from gitea_rest._runtime import ApiModel


class SearchResults(ApiModel):
    """SearchResults model."""

    data: Optional[List[Repository]] = None
    ok: Optional[StrictBool] = None
