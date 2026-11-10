# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.attachment import Attachment
from gitea_rest.models.user import User
from gitea_rest._runtime import ApiModel


class Release(ApiModel):
    """Release model."""

    assets: Optional[List[Attachment]] = None
    author: Optional[User] = None
    body: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    draft: Optional[StrictBool] = None
    html_url: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    prerelease: Optional[StrictBool] = None
    published_at: Optional[datetime] = None
    tag_name: Optional[StrictStr] = None
    tarball_url: Optional[StrictStr] = None
    target_commitish: Optional[StrictStr] = None
    upload_url: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    zipball_url: Optional[StrictStr] = None
