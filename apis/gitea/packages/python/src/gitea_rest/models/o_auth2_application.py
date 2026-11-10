# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class OAuth2Application(ApiModel):
    """OAuth2Application model."""

    client_id: Optional[StrictStr] = None
    client_secret: Optional[StrictStr] = None
    confidential_client: Optional[StrictBool] = None
    created: Optional[datetime] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    redirect_uris: Optional[List[StrictStr]] = None
    skip_secondary_authorization: Optional[StrictBool] = None
