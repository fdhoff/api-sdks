# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from collections.abc import Mapping as _Mapping
from pydantic import (
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    ModelWrapValidatorHandler as _ModelWrapValidatorHandler,
    StrictStr,
    model_validator as _model_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, cast as _cast
from mirakl_seller._runtime import ApiModel


class PRI01Response201(ApiModel):
    """PRI01Response201 model."""

    deprecated_import_id: Optional[StrictStr] = Field(
        default=None, validation_alias=AliasChoices("importId", "deprecated_import_id"), serialization_alias="importId"
    )
    import_id: Optional[StrictStr] = None
