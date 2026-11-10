"""Unofficial client for the Gitea API. Not affiliated with, endorsed by or sponsored by the Gitea project or Gitea
Limited."""

from . import models
from ._runtime import AsyncDownload, AuthRequest, Credentials, Download, FileInput
from .client import AsyncGiteaClient, GiteaClient
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

__version__ = "0.1.0a1"

__all__ = [
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AsyncDownload",
    "AsyncGiteaClient",
    "AuthRequest",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "Credentials",
    "DecodeError",
    "Download",
    "FileInput",
    "GiteaClient",
    "HttpError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "UnprocessableError",
    "models",
]
