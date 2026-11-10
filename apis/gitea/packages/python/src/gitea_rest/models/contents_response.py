# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.file_links_response import FileLinksResponse
from gitea_rest._runtime import ApiModel


class ContentsResponse(ApiModel):
    """ContentsResponse model."""

    links: Optional[FileLinksResponse] = Field(default=None, alias="_links")
    content: Optional[StrictStr] = None
    download_url: Optional[StrictStr] = None
    encoding: Optional[StrictStr] = None
    git_url: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    last_author_date: Optional[datetime] = None
    last_commit_message: Optional[StrictStr] = None
    last_commit_sha: Optional[StrictStr] = None
    last_committer_date: Optional[datetime] = None
    lfs_oid: Optional[StrictStr] = None
    lfs_size: Optional[StrictInt] = None
    mode: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    sha: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    submodule_git_url: Optional[StrictStr] = None
    target: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
