# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.topic_response import TopicResponse
from gitea_rest._runtime import ApiModel


class TopicListResponse(ApiModel):
    """TopicListResponse model."""

    topics: Optional[List[TopicResponse]] = None
