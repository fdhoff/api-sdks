# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from gitea_rest._runtime import ApiModel


class PackageFile(ApiModel):
    """PackageFile model."""

    id: Optional[StrictInt] = None
    md5: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    sha1: Optional[StrictStr] = None
    sha256: Optional[StrictStr] = None
    sha512: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
