# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.invest_activity_payload_credit import InvestActivityPayloadCredit
from mercury_banking.models.invest_activity_payload_dividend import InvestActivityPayloadDividend
from mercury_banking.models.invest_activity_payload_fee import InvestActivityPayloadFee
from mercury_banking.models.invest_activity_payload_interest_payment import InvestActivityPayloadInterestPayment
from mercury_banking.models.invest_activity_payload_portfolio_change import InvestActivityPayloadPortfolioChange
from mercury_banking.models.invest_activity_payload_trade import InvestActivityPayloadTrade
from mercury_banking.models.invest_activity_payload_transfer import InvestActivityPayloadTransfer
from typing import Union

InvestActivityPayload = Union[
    InvestActivityPayloadTransfer,
    InvestActivityPayloadTrade,
    InvestActivityPayloadFee,
    InvestActivityPayloadDividend,
    InvestActivityPayloadInterestPayment,
    InvestActivityPayloadCredit,
    InvestActivityPayloadPortfolioChange,
]
