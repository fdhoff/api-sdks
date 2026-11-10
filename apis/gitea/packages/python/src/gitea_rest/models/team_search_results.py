# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.team import Team
from gitea_rest._runtime import ApiModel


class TeamSearchResults(ApiModel):
    """TeamSearchResults model."""

    data: Optional[List[Team]] = None
    ok: Optional[StrictBool] = None
