# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.file_format_enum import FileFormatEnum
from ebay_sell.post_order.models.file_purpose_enum import FilePurposeEnum
from ebay_sell.post_order.models.file_status_enum import FileStatusEnum
from ebay_sell.post_order.models.return_user_role_enum import ReturnUserRoleEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ReturnFileType(ApiModel):
    """ReturnFileType model."""

    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    file_data: Optional[StrictStr] = Field(default=None, alias="fileData")
    file_format: Optional[FileFormatEnum] = Field(default=None, alias="fileFormat")
    file_id: Optional[StrictStr] = Field(default=None, alias="fileId")
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    file_purpose: Optional[FilePurposeEnum] = Field(default=None, alias="filePurpose")
    file_status: Optional[FileStatusEnum] = Field(default=None, alias="fileStatus")
    resized_file_data: Optional[StrictStr] = Field(default=None, alias="resizedFileData")
    secure_url: Optional[StrictStr] = Field(default=None, alias="secureUrl")
    submitter: Optional[ReturnUserRoleEnum] = None
