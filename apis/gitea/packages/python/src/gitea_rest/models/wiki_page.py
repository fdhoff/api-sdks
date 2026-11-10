# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.wiki_commit import WikiCommit
from gitea_rest._runtime import ApiModel


class WikiPage(ApiModel):
    """WikiPage model."""

    commit_count: Optional[StrictInt] = None
    content_base64: Optional[StrictStr] = None
    footer: Optional[StrictStr] = None
    html_url: Optional[StrictStr] = None
    last_commit: Optional[WikiCommit] = None
    sidebar: Optional[StrictStr] = None
    sub_url: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
