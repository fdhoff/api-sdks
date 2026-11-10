# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class MigrateRepoOptions(ApiModel):
    """MigrateRepoOptions model."""

    auth_password: Optional[StrictStr] = None
    auth_token: Optional[StrictStr] = None
    auth_username: Optional[StrictStr] = None
    aws_access_key_id: Optional[StrictStr] = None
    aws_secret_access_key: Optional[StrictStr] = None
    clone_addr: StrictStr
    description: Optional[StrictStr] = None
    issues: Optional[StrictBool] = None
    labels: Optional[StrictBool] = None
    lfs: Optional[StrictBool] = None
    lfs_endpoint: Optional[StrictStr] = None
    milestones: Optional[StrictBool] = None
    mirror: Optional[StrictBool] = None
    mirror_interval: Optional[StrictStr] = None
    private: Optional[StrictBool] = None
    pull_requests: Optional[StrictBool] = None
    releases: Optional[StrictBool] = None
    repo_name: StrictStr
    repo_owner: Optional[StrictStr] = None
    service: Optional[StrictStr] = None
    uid: Optional[StrictInt] = None
    wiki: Optional[StrictBool] = None
