# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class CH11Response200Channels(ApiModel):
    """CH11Response200Channels model."""

    code: StrictStr
    description: StrictStr
    label: StrictStr
