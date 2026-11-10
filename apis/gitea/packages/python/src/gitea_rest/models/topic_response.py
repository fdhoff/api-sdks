# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class TopicResponse(ApiModel):
    """TopicResponse model."""

    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    repo_count: Optional[StrictInt] = None
    topic_name: Optional[StrictStr] = None
    updated: Optional[datetime] = None
