import math

# Monthly mortgage payment (P&I) using loan amortization formula
def calculate_monthly_payment(loan_amount, annual_rate, term_years):
    if annual_rate == 0:
        return loan_amount / (term_years * 12)
    
    monthly_rate = annual_rate / 12
    num_payments = term_years * 12
    payment = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)
    return round(payment, 2)

# DSCR: NOI / Debt Service
def calculate_dscr(noi, annual_debt_service):
    if annual_debt_service == 0:
        return float('inf')
    return round(noi / annual_debt_service, 2)

# Cash-on-Cash Return: Annual Cash Flow / Total Out-of-Pocket
def calculate_coc_return(annual_cash_flow, out_of_pocket):
    if out_of_pocket == 0:
        return 0
    return round((annual_cash_flow / out_of_pocket) * 100, 2)

# Cap Rate: NOI / Purchase Price
def calculate_cap_rate(noi, purchase_price):
    if purchase_price == 0:
        return 0
    return round((noi / purchase_price) * 100, 2)

# Equity at Purchase: ARV - Total Cost Basis
def calculate_equity(arv, purchase_price, rehab_costs, closing_costs=0, assignment_fee=0):
    total_cost = purchase_price + rehab_costs + closing_costs + assignment_fee
    return round(arv - total_cost, 2)

# Refinance Proceeds (based on new appraised value and LTV)
def calculate_refi_proceeds(arv, ltv, closing_costs_pct=0.03):
    gross_loan = arv * ltv
    net_proceeds = gross_loan * (1 - closing_costs_pct)
    return round(net_proceeds, 2)

# NOI (Net Operating Income): Rent - Operating Expenses
def calculate_noi(gross_rent, operating_expenses):
    return round(gross_rent - operating_expenses, 2)

# Total Operating Expenses
def estimate_operating_expenses(rent, tax_rate=0.012, insurance=1200, vacancy_rate=0.05, maintenance_rate=0.08, capex_rate=0.05, mgmt_rate=0.08, monthly_utilities=0):
    annual_exp = (
        rent * 12 * (vacancy_rate + maintenance_rate + capex_rate + mgmt_rate)
        + (tax_rate * rent * 12)
        + insurance
        + (monthly_utilities * 12)
    )
    return round(annual_exp / 12, 2)  # Return monthly operating expenses
