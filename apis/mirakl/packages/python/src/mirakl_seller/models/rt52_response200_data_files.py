# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt52_response200_data_files_label import RT52Response200DataFilesLabel
from mirakl_seller.models.rt52_response200_data_files_qr_code import RT52Response200DataFilesQrCode
from mirakl_seller._runtime import ApiModel


class RT52Response200DataFiles(ApiModel):
    """RT52Response200DataFiles model."""

    label: Optional[RT52Response200DataFilesLabel] = None
    qr_code: Optional[RT52Response200DataFilesQrCode] = None
