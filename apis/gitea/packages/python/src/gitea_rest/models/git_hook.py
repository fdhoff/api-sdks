# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class GitHook(ApiModel):
    """GitHook model."""

    content: Optional[StrictStr] = None
    is_active: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
