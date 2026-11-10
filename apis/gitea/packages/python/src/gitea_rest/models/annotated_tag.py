# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.annotated_tag_object import AnnotatedTagObject
from gitea_rest.models.commit_user import CommitUser
from gitea_rest.models.payload_commit_verification import PayloadCommitVerification
from gitea_rest._runtime import ApiModel


class AnnotatedTag(ApiModel):
    """AnnotatedTag model."""

    message: Optional[StrictStr] = None
    object: Optional[AnnotatedTagObject] = None
    sha: Optional[StrictStr] = None
    tag: Optional[StrictStr] = None
    tagger: Optional[CommitUser] = None
    url: Optional[StrictStr] = None
    verification: Optional[PayloadCommitVerification] = None
