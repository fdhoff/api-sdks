# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class EditBranchProtectionOption(ApiModel):
    """EditBranchProtectionOption model."""

    approvals_whitelist_teams: Optional[List[StrictStr]] = None
    approvals_whitelist_username: Optional[List[StrictStr]] = None
    block_admin_merge_override: Optional[StrictBool] = None
    block_on_codeowner_reviews: Optional[StrictBool] = None
    block_on_official_review_requests: Optional[StrictBool] = None
    block_on_outdated_branch: Optional[StrictBool] = None
    block_on_rejected_reviews: Optional[StrictBool] = None
    bypass_allowlist_teams: Optional[List[StrictStr]] = None
    bypass_allowlist_usernames: Optional[List[StrictStr]] = None
    dismiss_stale_approvals: Optional[StrictBool] = None
    enable_approvals_whitelist: Optional[StrictBool] = None
    enable_bypass_allowlist: Optional[StrictBool] = None
    enable_force_push: Optional[StrictBool] = None
    enable_force_push_allowlist: Optional[StrictBool] = None
    enable_merge_whitelist: Optional[StrictBool] = None
    enable_push: Optional[StrictBool] = None
    enable_push_whitelist: Optional[StrictBool] = None
    enable_status_check: Optional[StrictBool] = None
    force_push_allowlist_deploy_keys: Optional[StrictBool] = None
    force_push_allowlist_teams: Optional[List[StrictStr]] = None
    force_push_allowlist_usernames: Optional[List[StrictStr]] = None
    ignore_stale_approvals: Optional[StrictBool] = None
    merge_whitelist_teams: Optional[List[StrictStr]] = None
    merge_whitelist_usernames: Optional[List[StrictStr]] = None
    priority: Optional[StrictInt] = None
    protected_file_patterns: Optional[StrictStr] = None
    push_whitelist_deploy_keys: Optional[StrictBool] = None
    push_whitelist_teams: Optional[List[StrictStr]] = None
    push_whitelist_usernames: Optional[List[StrictStr]] = None
    require_signed_commits: Optional[StrictBool] = None
    required_approvals: Optional[StrictInt] = None
    status_check_contexts: Optional[List[StrictStr]] = None
    unprotected_file_patterns: Optional[StrictStr] = None
