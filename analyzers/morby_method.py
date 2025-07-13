import streamlit as st
from components.ui_helpers import section_header, currency_input, percent_input
from components.deal_summaries import show_summary
from utils.constants import CURRENCY_FORMAT

def run():
    st.title("💵 Morby Method Analyzer")

    # Section: Property Info
    section_header("🏠 Property Details")
    arv = currency_input("ARV", value=250000)
    purchase_price = currency_input("Purchase Price", value=230000)
    repair_costs = currency_input("Estimated Repairs", value=15000)
    assignment_fee = currency_input("Assignment Fee (if applicable)", value=10000)

    # Section: DSCR Loan
    section_header("🏦 DSCR Loan Details")
    dscr_loan_pct = percent_input("DSCR Loan % of Purchase Price", value=80.0)
    dscr_rate = percent_input("DSCR Interest Rate", value=7.5)
    dscr_term = st.number_input("DSCR Loan Term (years)", value=30)

    # Section: Seller Finance
    section_header("🤝 Seller Finance (for gap funding)")
    seller_finance_pct = percent_input("Seller Finance % of Down Payment Gap", value=100.0)
    seller_finance_rate = percent_input("Seller Finance Interest Rate", value=5.0)
    seller_finance_term = st.number_input("Seller Finance Term (years)", value=5)

    # Section: Transactional Lending
    section_header("💸 Transactional Lending")
    trans_fee = currency_input("Transactional Lender Fee", value=3000)

    # Section: Rental Income & Ops
    section_header("📈 Income & Expenses")
    rent = currency_input("Monthly Rent (MTR/STR/LTR)", value=2300)
    est_expenses = currency_input("Estimated Monthly Expenses (all-in)", value=1200)

    # Placeholder Calculation (to be replaced with real calc engine)
    cash_flow = rent - est_expenses - 900  # placeholder for loan P&I
    summary = {
        "Monthly Cash Flow": CURRENCY_FORMAT.format(cash_flow),
        "DSCR": "1.22",  # placeholder
        "Total Out-of-Pocket": "$30,000",
        "Equity at Purchase": f"{CURRENCY_FORMAT.format(arv - purchase_price)}"
    }

    show_summary("💡 Preliminary Deal Summary", summary)
