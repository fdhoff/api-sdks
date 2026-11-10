# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class NotificationSubject(ApiModel):
    """NotificationSubject model."""

    html_url: Optional[StrictStr] = None
    latest_comment_html_url: Optional[StrictStr] = None
    latest_comment_url: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
