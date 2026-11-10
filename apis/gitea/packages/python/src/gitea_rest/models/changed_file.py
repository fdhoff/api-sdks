# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ChangedFile(ApiModel):
    """ChangedFile model."""

    additions: Optional[StrictInt] = None
    changes: Optional[StrictInt] = None
    contents_url: Optional[StrictStr] = None
    deletions: Optional[StrictInt] = None
    filename: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    previous_filename: Optional[StrictStr] = None
    raw_url: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
