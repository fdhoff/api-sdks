"""Notification API: destinations, subscriptions and topics."""

from . import models
from ._resources import AsyncResources, Resources

__all__ = ["AsyncResources", "Resources", "models"]
