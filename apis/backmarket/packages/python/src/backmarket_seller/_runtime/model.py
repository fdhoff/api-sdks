from __future__ import annotations

from collections.abc import Mapping, Sequence
from enum import Enum
from functools import cache
from typing import Any, TypeVar

from pydantic import (
    BaseModel,
    ConfigDict,
    TypeAdapter,
    ValidationError,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    model_validator,
)
from pydantic_core import to_jsonable_python

M = TypeVar("M", bound="ApiModel")

_TOLERANT = {"tolerant": True}


class ApiModel(BaseModel):
    """Base of every generated model.

    Models are strict when you build a request. Responses are parsed tolerantly: nothing has been
    confirmed against the live API, so a field that does not fit its declared type keeps its raw
    value instead of failing the call, a missing required field reads as None, and unknown fields
    stay available.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True, protected_namespaces=())

    @model_validator(mode="wrap")
    @classmethod
    def _tolerate(cls, data: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo) -> Any:
        try:
            return handler(data)
        except ValidationError:
            if not (info.context or {}).get("tolerant") or not isinstance(data, Mapping):
                raise
            return _salvage(cls, data)

    def to_wire(self) -> dict[str, Any]:
        """Return the fields that were set, under their API names."""
        return self.model_dump(mode="json", by_alias=True, exclude_unset=True, warnings=False)


def _salvage(cls: type[M], data: Mapping[str, Any]) -> M:
    remaining = dict(data)
    values: dict[str, Any] = {}
    fields_set = set()
    for name, field in cls.model_fields.items():
        key = field.alias if field.alias in remaining else name
        if key in remaining:
            values[name] = _field_value(cls, name, remaining.pop(key))
            fields_set.add(name)
        else:
            values[name] = None if field.is_required() else field.default
    return cls.model_construct(_fields_set=fields_set, **values, **remaining)


def _field_value(cls: type[ApiModel], name: str, raw: Any) -> Any:
    try:
        return _field_adapter(cls, name).validate_python(raw, context=_TOLERANT)
    except ValidationError:
        return raw


@cache
def _field_adapter(cls: type[ApiModel], name: str) -> TypeAdapter[Any]:
    return TypeAdapter(cls.model_fields[name].rebuild_annotation())


@cache
def _adapter(response_type: Any) -> TypeAdapter[Any]:
    return TypeAdapter(response_type)


def parse_response(response_type: Any, data: Any) -> Any:
    """Build the declared type from decoded data, or return the data as it came if it cannot fit."""
    if response_type is None:
        return data
    try:
        return _adapter(response_type).validate_python(data, context=_TOLERANT)
    except ValidationError:
        return data


def to_wire(value: Any) -> Any:
    """Turn a request value, which may mix models and plain data, into JSON-ready data."""
    if isinstance(value, ApiModel):
        return value.to_wire()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Mapping):
        return {key: to_wire(item) for key, item in value.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [to_wire(item) for item in value]
    return to_jsonable_python(value)
