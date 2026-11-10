# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from gitea_rest.models.external_tracker import ExternalTracker
from gitea_rest.models.external_wiki import ExternalWiki
from gitea_rest.models.internal_tracker import InternalTracker
from gitea_rest._runtime import ApiModel


class EditRepoOption(ApiModel):
    """EditRepoOption model."""

    allow_fast_forward_only_merge: Optional[StrictBool] = None
    allow_manual_merge: Optional[StrictBool] = None
    allow_merge_commits: Optional[StrictBool] = None
    allow_merge_update: Optional[StrictBool] = None
    allow_rebase: Optional[StrictBool] = None
    allow_rebase_explicit: Optional[StrictBool] = None
    allow_rebase_update: Optional[StrictBool] = None
    allow_squash_merge: Optional[StrictBool] = None
    archived: Optional[StrictBool] = None
    autodetect_manual_merge: Optional[StrictBool] = None
    default_allow_maintainer_edit: Optional[StrictBool] = None
    default_branch: Optional[StrictStr] = None
    default_delete_branch_after_merge: Optional[StrictBool] = None
    default_merge_style: Optional[StrictStr] = None
    default_update_style: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    enable_prune: Optional[StrictBool] = None
    external_tracker: Optional[ExternalTracker] = None
    external_wiki: Optional[ExternalWiki] = None
    has_actions: Optional[StrictBool] = None
    has_code: Optional[StrictBool] = None
    has_issues: Optional[StrictBool] = None
    has_packages: Optional[StrictBool] = None
    has_projects: Optional[StrictBool] = None
    has_pull_requests: Optional[StrictBool] = None
    has_releases: Optional[StrictBool] = None
    has_wiki: Optional[StrictBool] = None
    ignore_whitespace_conflicts: Optional[StrictBool] = None
    internal_tracker: Optional[InternalTracker] = None
    mirror_interval: Optional[StrictStr] = None
    mirror_password: Optional[StrictStr] = None
    mirror_token: Optional[StrictStr] = None
    mirror_username: Optional[StrictStr] = None
    name: Optional[Annotated[str, Field(strict=True)]] = None
    private: Optional[StrictBool] = None
    projects_mode: Optional[StrictStr] = None
    template: Optional[StrictBool] = None
    website: Optional[StrictStr] = None
