# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class InternalTracker(ApiModel):
    """InternalTracker model."""

    allow_only_contributors_to_track_time: Optional[StrictBool] = None
    enable_issue_dependencies: Optional[StrictBool] = None
    enable_time_tracker: Optional[StrictBool] = None
