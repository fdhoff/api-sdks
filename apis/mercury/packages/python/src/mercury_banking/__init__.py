"""Unofficial client for the Mercury API. Not affiliated with, endorsed by or sponsored by Mercury Technologies, Inc."""

from . import models
from ._runtime import FileInput
from .client import ENVIRONMENTS, AsyncMercuryClient, MercuryClient
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
from .webhooks import SIGNATURE_HEADER, WebhookSignatureError, verify_webhook

__version__ = "0.1.0a2"

__all__ = [
    "ENVIRONMENTS",
    "SIGNATURE_HEADER",
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AsyncMercuryClient",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "DecodeError",
    "FileInput",
    "HttpError",
    "MercuryClient",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "UnprocessableError",
    "WebhookSignatureError",
    "models",
    "verify_webhook",
]
