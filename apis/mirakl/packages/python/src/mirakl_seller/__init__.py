"""Unofficial client for the Mirakl marketplace seller API. Not affiliated with, endorsed by or sponsored by
Mirakl SAS."""

from . import models
from ._runtime import AsyncDownload, AuthRequest, Credentials, Download, FileInput
from .client import AsyncMiraklClient, MiraklClient
from .errors import (
    ApiConnectionError,
    ApiError,
    ApiTimeoutError,
    AuthenticationError,
    BadRequestError,
    DecodeError,
    HttpError,
    JobTimeoutError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
)

__version__ = "0.1.0a1"

__all__ = [
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AsyncDownload",
    "AsyncMiraklClient",
    "AuthRequest",
    "AuthenticationError",
    "BadRequestError",
    "Credentials",
    "DecodeError",
    "Download",
    "FileInput",
    "HttpError",
    "JobTimeoutError",
    "MiraklClient",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "models",
]
