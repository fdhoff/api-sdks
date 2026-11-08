"""Unofficial client for eBay's Sell, Commerce and Developer REST APIs. Not affiliated with, endorsed by or
sponsored by eBay Inc."""

from ._runtime import FileInput
from .client import ENVIRONMENTS, AsyncEbayClient, EbayClient
from .errors import (
    ApiConnectionError,
    ApiError,
    ApiTimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    DecodeError,
    ErrorDetail,
    ErrorParameter,
    HttpError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitedError,
    ServerError,
    UnprocessableError,
)
from .oauth import API_SCOPE, AuthorizationRequest, Token, authorization_url
from .signing import SigningKey

__version__ = "0.1.0a1"

__all__ = [
    "API_SCOPE",
    "ENVIRONMENTS",
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AsyncEbayClient",
    "AuthenticationError",
    "AuthorizationRequest",
    "BadRequestError",
    "ConflictError",
    "DecodeError",
    "EbayClient",
    "ErrorDetail",
    "ErrorParameter",
    "FileInput",
    "HttpError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "SigningKey",
    "Token",
    "UnprocessableError",
    "authorization_url",
]
