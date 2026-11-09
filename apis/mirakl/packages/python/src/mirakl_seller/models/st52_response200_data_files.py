# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st52_response200_data_files_label import ST52Response200DataFilesLabel
from mirakl_seller._runtime import ApiModel


class ST52Response200DataFiles(ApiModel):
    """ST52Response200DataFiles model."""

    label: Optional[ST52Response200DataFilesLabel] = None
