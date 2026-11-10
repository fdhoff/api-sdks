# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GitBlobResponse(ApiModel):
    """GitBlobResponse model."""

    content: Optional[StrictStr] = None
    encoding: Optional[StrictStr] = None
    lfs_oid: Optional[StrictStr] = None
    lfs_size: Optional[StrictInt] = None
    sha: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
