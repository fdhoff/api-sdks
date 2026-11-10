# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class CreateReleaseOption(ApiModel):
    """CreateReleaseOption model."""

    body: Optional[StrictStr] = None
    draft: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    prerelease: Optional[StrictBool] = None
    tag_message: Optional[StrictStr] = None
    tag_name: StrictStr
    target_commitish: Optional[StrictStr] = None
