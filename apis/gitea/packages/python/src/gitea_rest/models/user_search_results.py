# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class UserSearchResults(ApiModel):
    """UserSearchResults model."""

    data: Optional[List[User]] = None
    ok: Optional[StrictBool] = None
