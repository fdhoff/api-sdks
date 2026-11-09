# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from mercury_banking._runtime import (
    AsyncResource,
    Operation,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.organization_response import OrganizationResponse

_get_organization: Operation[OrganizationResponse] = Operation(
    id="getOrganization",
    method="GET",
    path="/organization",
    resource="organization",
    name="get",
    params=(),
    response=OrganizationResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (_get_organization,)


class OrganizationApi(Resource):
    @checked
    def get(
        self,
    ) -> OrganizationResponse:
        """Get your organization."""
        return self._call(
            _get_organization,
        )


class AsyncOrganizationApi(AsyncResource):
    @checked
    async def get(
        self,
    ) -> OrganizationResponse:
        """Get your organization."""
        return await self._call(
            _get_organization,
        )
