import streamlit as st

def run():
    st.header("Morby Method Analyzer")

    key_prefix = "morby_"

    # Section: Deal Numbers
    st.subheader("🔢 Deal Breakdown")

    arv = st.number_input("After Repair Value (ARV)", value=250000, key=f"{key_prefix}arv")
    purchase_price = st.number_input("Purchase Price", value=200000, key=f"{key_prefix}purchase_price")
    dscr_ltv = st.slider("DSCR Loan-To-Value (%)", min_value=50, max_value=90, value=75, step=1, key=f"{key_prefix}ltv")

    dscr_loan_amount = arv * (dscr_ltv / 100)
    seller_finance_amount = st.number_input("Seller Finance Portion", value=20000, key=f"{key_prefix}seller_finance")
    transaction_fee = st.number_input("Transactional Lender Fee / Double Close Cost", value=3000, key=f"{key_prefix}transaction_fee")

    total_capital_needed = seller_finance_amount + transaction_fee

    # Section: Monthly Income & Expenses
    st.subheader("📊 Monthly Numbers")

    rent = st.number_input("Monthly Rent", value=1800, key=f"{key_prefix}rent")
    piti = st.number_input("Monthly PITI (existing mortgage + escrows)", value=1200, key=f"{key_prefix}piti")
    cash_flow = rent - piti

    # Section: Summary Metrics
    st.subheader("📈 Summary")

    equity = arv - purchase_price
    st.metric("Estimated Equity at Purchase", f"${equity:,.2f}")

    st.metric("Total Capital Needed", f"${total_capital_needed:,.2f}")
    st.metric("Monthly Cash Flow", f"${cash_flow:,.2f}")

    if cash_flow < 0:
        st.warning("⚠️ This deal has negative cash flow.")
    if equity < 0:
        st.warning("⚠️ You're buying above ARV. Double check your numbers.")
