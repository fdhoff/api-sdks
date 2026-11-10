# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.payload_commit import PayloadCommit
from gitea_rest._runtime import ApiModel


class Branch(ApiModel):
    """Branch model."""

    commit: Optional[PayloadCommit] = None
    effective_branch_protection_name: Optional[StrictStr] = None
    enable_status_check: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    protected: Optional[StrictBool] = None
    required_approvals: Optional[StrictInt] = None
    status_check_contexts: Optional[List[StrictStr]] = None
    user_can_merge: Optional[StrictBool] = None
    user_can_push: Optional[StrictBool] = None
