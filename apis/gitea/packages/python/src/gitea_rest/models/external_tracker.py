# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class ExternalTracker(ApiModel):
    """ExternalTracker model."""

    external_tracker_format: Optional[StrictStr] = None
    external_tracker_regexp_pattern: Optional[StrictStr] = None
    external_tracker_style: Optional[StrictStr] = None
    external_tracker_url: Optional[StrictStr] = None
