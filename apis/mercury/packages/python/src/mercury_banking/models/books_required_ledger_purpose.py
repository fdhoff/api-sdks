# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksRequiredLedgerPurpose(str, Enum):
    """Allowed values of BooksRequiredLedgerPurpose."""

    UNCATINFLOW = "uncatInflow"
    UNCATOUTFLOW = "uncatOutflow"
    ACCOUNTTRANSFERS = "accountTransfers"
    OPENINGBALANCES = "openingBalances"
    ACCOUNTSRECEIVABLE = "accountsReceivable"
    ACCOUNTSPAYABLE = "accountsPayable"
    WAGESEXPENSE = "wagesExpense"
    BONUSEXPENSE = "bonusExpense"
    COMMISSIONSEXPENSE = "commissionsExpense"
    CONTRACTOREXPENSE = "contractorExpense"
    EMPLOYEEREIMBURSEMENTS = "employeeReimbursements"
    SEVERANCEEXPENSE = "severanceExpense"
    PAYROLLTAXEXPENSE = "payrollTaxExpense"
    EMPLOYERBENEFITSEXPENSE = "employerBenefitsExpense"
    HEALTHINSURANCEEXPENSE = "healthInsuranceExpense"
    WAGESPAYABLE = "wagesPayable"
    PAYROLLTAXPAYABLE = "payrollTaxPayable"
    EMPLOYEEBENEFITLIABILITIES = "employeeBenefitLiabilities"
    PAYROLLLIABILITIES = "payrollLiabilities"
    PAYROLLADJUSTMENTSCLEARING = "payrollAdjustmentsClearing"
    RETAINEDEARNINGS = "retainedEarnings"
    CURRENTYEAREARNINGS = "currentYearEarnings"
    BENEFITSEXPENSE = "benefitsExpense"
    DONATIONSEXPENSE = "donationsExpense"
    BENEFITSPAYABLE = "benefitsPayable"
    PAYROLLTAXACCRUALS = "payrollTaxAccruals"
    STOCKEXERCISECLEARING = "stockExerciseClearing"
    PAYROLLCLEARING = "payrollClearing"
