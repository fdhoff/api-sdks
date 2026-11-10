# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class MergePullRequestOption(ApiModel):
    """MergePullRequestOption model."""

    delete_branch_after_merge: Optional[StrictBool] = None
    do: StrictStr
    force_merge: Optional[StrictBool] = None
    head_commit_id: Optional[StrictStr] = None
    merge_commit_id: Optional[StrictStr] = None
    merge_message_field: Optional[StrictStr] = None
    merge_title_field: Optional[StrictStr] = None
    merge_when_checks_succeed: Optional[StrictBool] = None
