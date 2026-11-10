# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class PullRequestMeta(ApiModel):
    """PullRequestMeta model."""

    draft: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    merged: Optional[StrictBool] = None
    merged_at: Optional[datetime] = None
