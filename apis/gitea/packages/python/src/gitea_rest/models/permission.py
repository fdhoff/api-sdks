# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class Permission(ApiModel):
    """Permission model."""

    admin: Optional[StrictBool] = None
    pull: Optional[StrictBool] = None
    push: Optional[StrictBool] = None
