# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class McpAgentFeedbackRequest(ApiModel):
    """McpAgentFeedbackRequest model."""

    attempted: Optional[StrictStr] = None
    category: StrictStr
    expected: Optional[StrictStr] = None
    impact: StrictStr
    mcp_client_name: Optional[StrictStr] = Field(default=None, alias="mcpClientName")
    mcp_client_version: Optional[StrictStr] = Field(default=None, alias="mcpClientVersion")
    mcp_session_id: Optional[StrictStr] = Field(default=None, alias="mcpSessionId")
    summary: Annotated[str, Field(min_length=1, strict=True)]
    tool_name: Optional[StrictStr] = Field(default=None, alias="toolName")
