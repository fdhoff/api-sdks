# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class UserSettings(ApiModel):
    """UserSettings model."""

    description: Optional[StrictStr] = None
    diff_view_style: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    hide_activity: Optional[StrictBool] = None
    hide_email: Optional[StrictBool] = None
    language: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    theme: Optional[StrictStr] = None
    website: Optional[StrictStr] = None
