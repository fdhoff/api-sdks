# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.external_tracker import ExternalTracker
from gitea_rest.models.external_wiki import ExternalWiki
from gitea_rest.models.internal_tracker import InternalTracker
from gitea_rest.models.object_format_name import ObjectFormatName
from gitea_rest.models.permission import Permission
from gitea_rest.models.repo_transfer import RepoTransfer
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Repository(ApiModel):
    """Repository model."""

    allow_fast_forward_only_merge: Optional[StrictBool] = None
    allow_manual_merge: Optional[StrictBool] = None
    allow_merge_commits: Optional[StrictBool] = None
    allow_merge_update: Optional[StrictBool] = None
    allow_rebase: Optional[StrictBool] = None
    allow_rebase_explicit: Optional[StrictBool] = None
    allow_rebase_update: Optional[StrictBool] = None
    allow_squash_merge: Optional[StrictBool] = None
    archived: Optional[StrictBool] = None
    archived_at: Optional[datetime] = None
    autodetect_manual_merge: Optional[StrictBool] = None
    avatar_url: Optional[StrictStr] = None
    branch_count: Optional[StrictInt] = None
    clone_url: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    default_allow_maintainer_edit: Optional[StrictBool] = None
    default_branch: Optional[StrictStr] = None
    default_delete_branch_after_merge: Optional[StrictBool] = None
    default_merge_style: Optional[StrictStr] = None
    default_target_branch: Optional[StrictStr] = None
    default_update_style: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    empty: Optional[StrictBool] = None
    external_tracker: Optional[ExternalTracker] = None
    external_wiki: Optional[ExternalWiki] = None
    fork: Optional[StrictBool] = None
    forks_count: Optional[StrictInt] = None
    full_name: Optional[StrictStr] = None
    has_actions: Optional[StrictBool] = None
    has_code: Optional[StrictBool] = None
    has_issues: Optional[StrictBool] = None
    has_packages: Optional[StrictBool] = None
    has_projects: Optional[StrictBool] = None
    has_pull_requests: Optional[StrictBool] = None
    has_releases: Optional[StrictBool] = None
    has_wiki: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    ignore_whitespace_conflicts: Optional[StrictBool] = None
    internal: Optional[StrictBool] = None
    internal_tracker: Optional[InternalTracker] = None
    language: Optional[StrictStr] = None
    languages_url: Optional[StrictStr] = None
    licenses: Optional[List[StrictStr]] = None
    link: Optional[StrictStr] = None
    mirror: Optional[StrictBool] = None
    mirror_interval: Optional[StrictStr] = None
    mirror_last_sync_at: Optional[datetime] = None
    mirror_updated: Optional[datetime] = None
    name: Optional[StrictStr] = None
    object_format_name: Optional[ObjectFormatName] = None
    open_issues_count: Optional[StrictInt] = None
    open_pr_counter: Optional[StrictInt] = None
    original_url: Optional[StrictStr] = None
    owner: Optional[User] = None
    parent: Optional[Repository] = None
    permissions: Optional[Permission] = None
    private: Optional[StrictBool] = None
    projects_mode: Optional[StrictStr] = None
    release_counter: Optional[StrictInt] = None
    repo_transfer: Optional[RepoTransfer] = None
    size: Optional[StrictInt] = None
    ssh_url: Optional[StrictStr] = None
    stars_count: Optional[StrictInt] = None
    template: Optional[StrictBool] = None
    topics: Optional[List[StrictStr]] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
    watchers_count: Optional[StrictInt] = None
    website: Optional[StrictStr] = None


Repository.model_rebuild(raise_errors=False)
