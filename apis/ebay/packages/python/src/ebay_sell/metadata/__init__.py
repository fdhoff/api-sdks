"""Metadata API: marketplace and category policies, compatibility and shipping data."""

from . import models
from ._resources import AsyncResources, Resources

__all__ = ["AsyncResources", "Resources", "models"]
