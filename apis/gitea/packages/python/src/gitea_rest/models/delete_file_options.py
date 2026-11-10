# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_date_options import CommitDateOptions
from gitea_rest.models.identity import Identity
from gitea_rest._runtime import ApiModel


class DeleteFileOptions(ApiModel):
    """DeleteFileOptions model."""

    author: Optional[Identity] = None
    branch: Optional[StrictStr] = None
    committer: Optional[Identity] = None
    dates: Optional[CommitDateOptions] = None
    force_push: Optional[StrictBool] = None
    message: Optional[StrictStr] = None
    new_branch: Optional[StrictStr] = None
    sha: StrictStr
    signoff: Optional[StrictBool] = None
