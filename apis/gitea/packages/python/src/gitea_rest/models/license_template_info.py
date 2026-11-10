# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class LicenseTemplateInfo(ApiModel):
    """LicenseTemplateInfo model."""

    body: Optional[StrictStr] = None
    implementation: Optional[StrictStr] = None
    key: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
