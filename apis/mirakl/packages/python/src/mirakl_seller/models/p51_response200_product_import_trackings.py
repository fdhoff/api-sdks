# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p51_response200_product_import_trackings_conversion_options import (
    P51Response200ProductImportTrackingsConversionOptions,
)
from mirakl_seller.models.p51_response200_product_import_trackings_integration_details import (
    P51Response200ProductImportTrackingsIntegrationDetails,
)
from mirakl_seller._runtime import ApiModel


class P51Response200ProductImportTrackings(ApiModel):
    """P51Response200ProductImportTrackings model."""

    conversion_options: Optional[P51Response200ProductImportTrackingsConversionOptions] = None
    conversion_type: Optional[StrictStr] = None
    date_created: datetime
    has_error_report: StrictBool
    has_new_product_report: StrictBool
    has_transformation_error_report: Optional[StrictBool] = None
    has_transformed_file: StrictBool
    import_id: StrictInt
    import_status: StrictStr
    integration_details: Optional[P51Response200ProductImportTrackingsIntegrationDetails] = None
    reason_status: Optional[StrictStr] = None
    shop_id: StrictInt
    transform_lines_in_error: StrictInt
    transform_lines_in_success: StrictInt
    transform_lines_read: StrictInt
    transform_lines_with_warning: StrictInt
