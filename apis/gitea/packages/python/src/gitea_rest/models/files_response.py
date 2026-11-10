# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.contents_response import ContentsResponse
from gitea_rest.models.file_commit_response import FileCommitResponse
from gitea_rest.models.payload_commit_verification import PayloadCommitVerification
from gitea_rest._runtime import ApiModel


class FilesResponse(ApiModel):
    """FilesResponse model."""

    commit: Optional[FileCommitResponse] = None
    files: Optional[List[ContentsResponse]] = None
    verification: Optional[PayloadCommitVerification] = None
