# Default Assumptions
DEFAULT_PROPERTY_TAX_RATE = 1.2  # as a percentage
DEFAULT_INSURANCE_COST = 1200    # annual estimate
DEFAULT_VACANCY_RATE = 0.05      # 5%
DEFAULT_MAINTENANCE_RATE = 0.08  # 8%
DEFAULT_MANAGEMENT_RATE = 0.08   # 8%
DEFAULT_CAPEX_RATE = 0.05        # 5%
DEFAULT_APPRECIATION_RATE = 0.03 # 3% annual
DEFAULT_INFLATION_RATE = 0.02    # 2%

# Financing Defaults
DEFAULT_INTEREST_RATE = 0.07     # 7%
DEFAULT_LOAN_TERM_YEARS = 30
DEFAULT_DOWN_PAYMENT_PERCENT = 0.20  # 20%

# Streamlit Formatting
CURRENCY_FORMAT = "${:,.2f}"
PERCENT_FORMAT = "{:.2%}"

# Labels for Summary Metrics
SUMMARY_LABELS = {
    "cash_flow": "Monthly Cash Flow",
    "coc_return": "Cash-on-Cash Return",
    "dscr": "DSCR",
    "total_equity": "Total Equity",
    "roi": "Return on Investment",
    "net_profit": "Net Profit",
    "cap_rate": "Cap Rate"
}
