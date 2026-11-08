# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Union

from ebay_sell._runtime import AsyncResource, Operation, Resource, Scheme, checked
from ebay_sell.account.models.program import Program
from ebay_sell.account.models.programs import Programs

_get_opted_in_programs: Operation[Programs] = Operation(
    id="getOptedInPrograms",
    method="GET",
    path="/sell/account/v1/program/get_opted_in_programs",
    resource="programs",
    name="list_opted_in",
    params=(),
    response=Programs,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.account.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_opt_in_to_program: Operation[object] = Operation(
    id="optInToProgram",
    method="POST",
    path="/sell/account/v1/program/opt_in",
    resource="programs",
    name="opt_in",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)
_opt_out_of_program: Operation[object] = Operation(
    id="optOutOfProgram",
    method="POST",
    path="/sell/account/v1/program/opt_out",
    resource="programs",
    name="opt_out",
    params=(),
    response=object,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.account",)),),),
    host="api",
)

OPERATIONS = (
    _get_opted_in_programs,
    _opt_in_to_program,
    _opt_out_of_program,
)


class ProgramsApi(Resource):
    @checked
    def list_opted_in(
        self,
    ) -> Programs:
        """List the seller programs the seller has joined."""
        return self._call(
            _get_opted_in_programs,
        )

    @checked
    def opt_in(
        self,
        body: Union[Program, Mapping[str, Any]],
    ) -> object:
        """Join a seller program."""
        return self._call(
            _opt_in_to_program,
            _body=body,
        )

    @checked
    def opt_out(
        self,
        body: Union[Program, Mapping[str, Any]],
    ) -> object:
        """Leave a seller program."""
        return self._call(
            _opt_out_of_program,
            _body=body,
        )


class AsyncProgramsApi(AsyncResource):
    @checked
    async def list_opted_in(
        self,
    ) -> Programs:
        """List the seller programs the seller has joined."""
        return await self._call(
            _get_opted_in_programs,
        )

    @checked
    async def opt_in(
        self,
        body: Union[Program, Mapping[str, Any]],
    ) -> object:
        """Join a seller program."""
        return await self._call(
            _opt_in_to_program,
            _body=body,
        )

    @checked
    async def opt_out(
        self,
        body: Union[Program, Mapping[str, Any]],
    ) -> object:
        """Leave a seller program."""
        return await self._call(
            _opt_out_of_program,
            _body=body,
        )
