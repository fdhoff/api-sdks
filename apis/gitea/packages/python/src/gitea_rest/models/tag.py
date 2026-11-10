# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.commit_meta import CommitMeta
from gitea_rest._runtime import ApiModel


class Tag(ApiModel):
    """Tag model."""

    commit: Optional[CommitMeta] = None
    id: Optional[StrictStr] = None
    message: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    tarball_url: Optional[StrictStr] = None
    zipball_url: Optional[StrictStr] = None
