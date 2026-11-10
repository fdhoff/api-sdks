# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GeneralAPISettings(ApiModel):
    """GeneralAPISettings model."""

    default_git_trees_per_page: Optional[StrictInt] = None
    default_max_blob_size: Optional[StrictInt] = None
    default_max_response_size: Optional[StrictInt] = None
    default_paging_num: Optional[StrictInt] = None
    max_response_items: Optional[StrictInt] = None
