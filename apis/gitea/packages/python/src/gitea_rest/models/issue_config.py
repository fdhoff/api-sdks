# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.issue_config_contact_link import IssueConfigContactLink
from gitea_rest._runtime import ApiModel


class IssueConfig(ApiModel):
    """IssueConfig model."""

    blank_issues_enabled: Optional[StrictBool] = None
    contact_links: Optional[List[IssueConfigContactLink]] = None
