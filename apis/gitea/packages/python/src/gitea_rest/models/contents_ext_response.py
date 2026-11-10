# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.contents_response import ContentsResponse
from gitea_rest._runtime import ApiModel


class ContentsExtResponse(ApiModel):
    """ContentsExtResponse model."""

    dir_contents: Optional[List[ContentsResponse]] = None
    file_contents: Optional[ContentsResponse] = None
