# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class FileLinksResponse(ApiModel):
    """FileLinksResponse model."""

    git: Optional[StrictStr] = None
    html: Optional[StrictStr] = None
    var_self: Optional[StrictStr] = Field(default=None, alias="self")
