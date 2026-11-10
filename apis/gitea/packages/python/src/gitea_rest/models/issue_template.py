# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.issue_form_field import IssueFormField
from gitea_rest._runtime import ApiModel


class IssueTemplate(ApiModel):
    """IssueTemplate model."""

    about: Optional[StrictStr] = None
    assignees: Optional[List[StrictStr]] = None
    body: Optional[List[IssueFormField]] = None
    content: Optional[StrictStr] = None
    file_name: Optional[StrictStr] = None
    labels: Optional[List[StrictStr]] = None
    name: Optional[StrictStr] = None
    ref: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
