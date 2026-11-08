# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.account.models.payments_program_onboarding_response import PaymentsProgramOnboardingResponse
from ebay_sell.account.models.payments_program_response import PaymentsProgramResponse

_get_payments_program: Operation[PaymentsProgramResponse] = Operation(
    id="getPaymentsProgram",
    method="GET",
    path="/sell/account/v1/payments_program/{marketplace_id}/{payments_program_type}",
    resource="payments_programs",
    name="get",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("payments_program_type", "payments_program_type", "path"),
    ),
    response=PaymentsProgramResponse,
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
_get_payments_program_onboarding: Operation[PaymentsProgramOnboardingResponse] = Operation(
    id="getPaymentsProgramOnboarding",
    method="GET",
    path="/sell/account/v1/payments_program/{marketplace_id}/{payments_program_type}/onboarding",
    resource="payments_programs",
    name="get_onboarding",
    params=(
        Param("marketplace_id", "marketplace_id", "path"),
        Param("payments_program_type", "payments_program_type", "path"),
    ),
    response=PaymentsProgramOnboardingResponse,
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

OPERATIONS = (
    _get_payments_program,
    _get_payments_program_onboarding,
)


class PaymentsProgramsApi(Resource):
    @checked
    def get(
        self,
        marketplace_id: StrictStr,
        payments_program_type: StrictStr,
    ) -> PaymentsProgramResponse:
        """Get the seller's status in a payments program."""
        return self._call(
            _get_payments_program,
            marketplace_id=marketplace_id,
            payments_program_type=payments_program_type,
        )

    @checked
    def get_onboarding(
        self,
        marketplace_id: StrictStr,
        payments_program_type: StrictStr,
    ) -> PaymentsProgramOnboardingResponse:
        """Get the seller's onboarding progress in a payments program."""
        return self._call(
            _get_payments_program_onboarding,
            marketplace_id=marketplace_id,
            payments_program_type=payments_program_type,
        )


class AsyncPaymentsProgramsApi(AsyncResource):
    @checked
    async def get(
        self,
        marketplace_id: StrictStr,
        payments_program_type: StrictStr,
    ) -> PaymentsProgramResponse:
        """Get the seller's status in a payments program."""
        return await self._call(
            _get_payments_program,
            marketplace_id=marketplace_id,
            payments_program_type=payments_program_type,
        )

    @checked
    async def get_onboarding(
        self,
        marketplace_id: StrictStr,
        payments_program_type: StrictStr,
    ) -> PaymentsProgramOnboardingResponse:
        """Get the seller's onboarding progress in a payments program."""
        return await self._call(
            _get_payments_program_onboarding,
            marketplace_id=marketplace_id,
            payments_program_type=payments_program_type,
        )
