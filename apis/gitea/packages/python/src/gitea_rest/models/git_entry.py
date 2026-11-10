# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GitEntry(ApiModel):
    """GitEntry model."""

    mode: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
