from __future__ import annotations

from ._resources import Resources
from .models.import_status import ImportStatus
from .models.uploads import Uploads
from .models.widget import Widget


def use(resources: Resources) -> tuple[Widget, Uploads, Uploads]:
    return resources.widgets.get("w1", verbose=True), resources.uploads.list(), resources.uploads.list(x_tenant_id="t1")


def wait(resources: Resources) -> ImportStatus:
    return resources.imports.wait(7, interval=1, timeout=60)
