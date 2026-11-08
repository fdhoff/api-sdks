"""Marketing API: Promoted Listings, promotions and store email campaigns."""

from . import models
from ._resources import AsyncResources, Resources

__all__ = ["AsyncResources", "Resources", "models"]
