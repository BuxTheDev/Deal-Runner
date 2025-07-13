# ---------------------------------------
# Default Assumptions for Calculators
# ---------------------------------------

# Property & Operating Expenses
DEFAULT_PROPERTY_TAX_RATE = 1.2         # % of property value annually
DEFAULT_INSURANCE_COST = 1200           # Annual insurance estimate in $
DEFAULT_VACANCY_RATE = 0.05             # 5%
DEFAULT_MAINTENANCE_RATE = 0.08         # 8% of rent
DEFAULT_CAPEX_RATE = 0.05               # 5% of rent
DEFAULT_MANAGEMENT_RATE = 0.08          # 8% of rent
DEFAULT_UTILITIES_COST = 300            # Monthly utilities (if landlord pays)

# Financing Assumptions
DEFAULT_INTEREST_RATE = 0.07            # 7% interest rate
DEFAULT_LOAN_TERM_YEARS = 30            # 30-year term
DEFAULT_DOWN_PAYMENT_PERCENT = 0.20     # 20%

# Appreciation & Inflation
DEFAULT_APPRECIATION_RATE = 0.03        # 3% annual property appreciation
DEFAULT_INFLATION_RATE = 0.02           # 2% inflation assumption

# Refinance Assumptions
DEFAULT_REFI_LTV = 0.75                 # 75% loan-to-value for refi
DEFAULT_REFI_CLOSING_COSTS = 0.03       # 3% of loan amount
DEFAULT_REFI_SEASONING_MONTHS = 6       # Typical seasoning period

# ---------------------------------------
# UI Formatting
LAYOUT ='centered'  # Streamlit layout setting
# ---------------------------------------

CURRENCY_FORMAT = "${:,.2f}"
PERCENT_FORMAT = "{:.2%}"

# ---------------------------------------
# Summary Metric Labels (Standardized)
# ---------------------------------------

SUMMARY_LABELS = {
    "cash_flow": "Monthly Cash Flow",
    "coc_return": "Cash-on-Cash Return",
    "dscr": "DSCR",
    "net_profit": "Net Profit",
    "total_equity": "Total Equity",
    "equity_at_purchase": "Equity at Purchase",
    "cap_rate": "Capitalization Rate",
    "roi": "Return on Investment",
    "annualized_roi": "Annualized ROI",
    "refi_proceeds": "Refi Proceeds",
    "rehab_costs": "Rehab Budget",
}
