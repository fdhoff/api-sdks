# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class AppointmentDetails(ApiModel):
    """AppointmentDetails model."""

    appointment_end_time: Optional[StrictStr] = Field(default=None, alias="appointmentEndTime")
    appointment_start_time: Optional[StrictStr] = Field(default=None, alias="appointmentStartTime")
    appointment_status: Optional[StrictStr] = Field(default=None, alias="appointmentStatus")
    appointment_type: Optional[StrictStr] = Field(default=None, alias="appointmentType")
    appointment_window: Optional[StrictStr] = Field(default=None, alias="appointmentWindow")
    service_provider_appointment_date: Optional[StrictStr] = Field(default=None, alias="serviceProviderAppointmentDate")
