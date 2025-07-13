import streamlit as st
import components.layout as layout

def run():
    key_prefix = "morby_"

    layout.section_header("🧮", "DSCR Loan Inputs")

    layout.two_column_inputs(
        [
            lambda: st.number_input("Purchase Price ($)", value=0, key=f"{key_prefix}purchase"),
            lambda: st.number_input("Monthly Market Rent ($)", value=0, key=f"{key_prefix}rent"),
            lambda: st.number_input("Estimated Closing Costs ($)", value=0, key=f"{key_prefix}closing"),
        ],
        [
            lambda: st.number_input("DSCR Requirement", value=1.15, key=f"{key_prefix}dscr_req"),
            lambda: st.number_input("DSCR Interest Rate (%)", value=8.25, key=f"{key_prefix}interest"),
            lambda: st.number_input("DSCR Loan Term (Years)", value=30, key=f"{key_prefix}term"),
        ]
    )

    st.slider("Max LTV % for DSCR Loan", 50, 90, 75, key=f"{key_prefix}ltv")
    st.number_input("Transactional Lender Fee (%)", value=2.0, key=f"{key_prefix}txn_fee")

    layout.horizontal_rule()
    layout.section_header("💰", "Seller Finance Terms")

    layout.two_column_inputs(
        [lambda: st.number_input("Seller Finance Interest Rate (%)", value=5.0, key=f"{key_prefix}sf_rate")],
        [lambda: st.number_input("Seller Finance Amortization (Years)", value=30, key=f"{key_prefix}sf_term")]
    )

    layout.horizontal_rule()
    layout.section_header("📊", "Deal Summary")

    layout.three_column_metrics([
        ("DSCR Loan Amount", "$0.00"),
        ("Seller Finance Amount", "$0.00"),
        ("Monthly Rent", "$0.00"),
        ("DSCR Payment", "$0.00"),
        ("Seller Payment", "$0.00"),
        ("Total Debt", "$0.00"),
        ("Cash Flow", "$0.00"),
        ("Closing Costs", "$0.00"),
        ("DSCR Ratio", "1.15x"),
    ])

    layout.horizontal_rule()
    layout.section_header("💼", "Transactional Funding")

    st.write("**Required Funds (Seller Note + Closing):** $0.00")
    st.write("**Lender Fee @ 2.00%:** $0.00")
    st.write("**Total Repayment to Transactional Lender:** $0.00")
    st.write("**Cash Needed at Closing:** $0.00")