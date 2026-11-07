from __future__ import annotations

import functools
import inspect
from collections.abc import Callable, Mapping, Sequence
from enum import Enum
from functools import cache
from typing import Any, TypeVar, cast, get_type_hints

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
from typing_extensions import TypedDict

M = TypeVar("M", bound="ApiModel")
F = TypeVar("F", bound=Callable[..., Any])

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
    salvaged = cls.model_construct(_fields_set=fields_set, **values)
    salvaged.__pydantic_extra__ = remaining
    return salvaged


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
    """Build the declared type from decoded data. Raises ValidationError when the data cannot fit it at all."""
    if response_type is None:
        return None
    return _adapter(response_type).validate_python(data, context=_TOLERANT)


def checked(method: F) -> F:
    """Check a call's arguments against the method's annotations, constraints included, before it runs.
    The arguments are passed on as given, not converted."""
    signature = inspect.signature(method)

    # Built on first use, so importing the client stays fast and every annotation has resolved.
    @cache
    def arguments() -> tuple[TypeAdapter[Any], frozenset[str]]:
        hints = get_type_hints(method, include_extras=True)
        fields = {name: hints[name] for name in signature.parameters if name in hints}
        typed_dict: Any = TypedDict  # mypy accepts only a literal field map
        return TypeAdapter(typed_dict(method.__qualname__, fields)), frozenset(fields)

    def check(args: tuple[Any, ...], kwargs: dict[str, Any]) -> None:
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()
        adapter, names = arguments()
        adapter.validate_python({name: value for name, value in bound.arguments.items() if name in names})

    if inspect.iscoroutinefunction(method):

        @functools.wraps(method)
        async def check_then_await(*args: Any, **kwargs: Any) -> Any:
            check(args, kwargs)
            return await method(*args, **kwargs)

        return cast(F, check_then_await)

    @functools.wraps(method)
    def check_then_call(*args: Any, **kwargs: Any) -> Any:
        check(args, kwargs)
        return method(*args, **kwargs)

    return cast(F, check_then_call)


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
