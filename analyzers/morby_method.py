import streamlit as st
import components.layout as layout

def run():
    key = "morby_"
    layout.section_header("🧮", "DSCR Loan Inputs")

    layout.two_column_inputs(
        [
            lambda: st.number_input("DSCR Loan Amount", value=180000, key=f"{key}loan_amount"),
            lambda: st.number_input("Seller Finance Portion", value=20000, key=f"{key}seller_finance"),
        ],
        [
            lambda: st.number_input("Purchase Price", value=200000, key=f"{key}purchase_price"),
            lambda: st.number_input("Estimated Closing Costs ($)", value=10000, key=f"{key}closing_costs"),
        ]
    )

    transaction_fee_pct = st.number_input("Transactional Lender Fee (%)", value=2.0, key=f"{key}txn_fee")
    total_capital_needed = st.session_state[f"{key}seller_finance"] + st.session_state[f"{key}closing_costs"]

    layout.section_header("📊", "Monthly Income & DSCR")

    layout.two_column_inputs(
        [
            lambda: st.number_input("Monthly Rent", value=5000, key=f"{key}rent"),
            lambda: st.number_input("DSCR Loan Term (Years)", value=30, key=f"{key}term"),
        ],
        [
            lambda: st.number_input("DSCR Interest Rate (%)", value=8.25, key=f"{key}interest"),
        ]
    )

    dscr_loan = st.session_state[f"{key}loan_amount"]
    dscr_interest = st.session_state[f"{key}interest"]
    monthly_dscr_payment = (dscr_loan * (dscr_interest / 100)) / 12

    layout.section_header("💰", "Seller Finance Terms")

    layout.two_column_inputs(
        [
            lambda: st.number_input("Seller Finance Interest Rate (%)", value=5.08, key=f"{key}sf_rate"),
        ],
        [
            lambda: st.number_input("Seller Finance Amortization (Years)", value=30, key=f"{key}sf_term"),
        ]
    )

    seller_finance = st.session_state[f"{key}seller_finance"]
    seller_interest = st.session_state[f"{key}sf_rate"]
    monthly_seller_payment = (seller_finance * (seller_interest / 100)) / 12

    total_debt = dscr_loan + seller_finance
    total_monthly_debt = monthly_dscr_payment + monthly_seller_payment
    cash_flow = st.session_state[f"{key}rent"] - total_monthly_debt
    dscr_ratio = st.session_state[f"{key}rent"] / (total_monthly_debt + 1e-6)

    layout.horizontal_rule()
    layout.section_header("📈", "Deal Summary")

    layout.three_column_metrics([
        ("DSCR Loan Amount", f"${dscr_loan:,.2f}"),
        ("Seller Finance Amount", f"${seller_finance:,.2f}"),
        ("Monthly Rent", f"${st.session_state[f'{key}rent']:,.2f}"),
        ("DSCR Payment", f"${monthly_dscr_payment:,.2f}"),
        ("Seller Payment", f"${monthly_seller_payment:,.2f}"),
        ("Total Debt", f"${total_monthly_debt:,.2f}"),
        ("Cash Flow", f"${cash_flow:,.2f}"),
        ("Closing Costs", f"${st.session_state[f'{key}closing_costs']:,.2f}"),
        ("DSCR Ratio", f"{dscr_ratio:.2f}x"),
    ])

    layout.horizontal_rule()
    layout.section_header("💼", "Transactional Funding")

    lender_fee = transaction_fee_pct / 100 * total_capital_needed
    total_repayment = total_capital_needed + lender_fee

    st.write(f"**Required Funds (Seller Note + Closing):** ${total_capital_needed:,.2f}")
    st.write(f"**Lender Fee @ {transaction_fee_pct:.2f}%:** ${lender_fee:,.2f}")
    st.write(f"**Total Repayment to Transactional Lender:** ${total_repayment:,.2f}")
    st.write(f"**Cash Needed at Closing:** ${total_repayment:,.2f}")
