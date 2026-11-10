# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class OrganizationPermissions(ApiModel):
    """OrganizationPermissions model."""

    can_create_repository: Optional[StrictBool] = None
    can_read: Optional[StrictBool] = None
    can_write: Optional[StrictBool] = None
    is_admin: Optional[StrictBool] = None
    is_owner: Optional[StrictBool] = None
