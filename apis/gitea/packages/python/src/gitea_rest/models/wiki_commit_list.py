# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.wiki_commit import WikiCommit
from gitea_rest._runtime import ApiModel


class WikiCommitList(ApiModel):
    """WikiCommitList model."""

    commits: Optional[List[WikiCommit]] = None
    count: Optional[StrictInt] = None
