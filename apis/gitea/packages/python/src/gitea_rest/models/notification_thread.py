# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest.models.notification_subject import NotificationSubject
from gitea_rest.models.repository import Repository
from gitea_rest._runtime import ApiModel


class NotificationThread(ApiModel):
    """NotificationThread model."""

    id: Optional[StrictInt] = None
    pinned: Optional[StrictBool] = None
    repository: Optional[Repository] = None
    subject: Optional[NotificationSubject] = None
    unread: Optional[StrictBool] = None
    updated_at: Optional[datetime] = None
    url: Optional[StrictStr] = None
