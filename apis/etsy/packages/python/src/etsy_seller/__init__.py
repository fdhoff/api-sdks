"""Unofficial client for the Etsy Open API v3. Not affiliated with Etsy."""

from . import models
from ._runtime import FileInput
from .client import AsyncEtsyClient, EtsyClient
from .errors import (
    ApiConnectionError,
    ApiError,
    ApiTimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    DecodeError,
    HttpError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    UnprocessableError,
)
from .oauth import AuthorizationRequest, Token, authorization_url

__version__ = "0.1.0a2"

__all__ = [
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AsyncEtsyClient",
    "AuthenticationError",
    "AuthorizationRequest",
    "BadRequestError",
    "ConflictError",
    "DecodeError",
    "EtsyClient",
    "FileInput",
    "HttpError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "Token",
    "UnprocessableError",
    "authorization_url",
    "models",
]
