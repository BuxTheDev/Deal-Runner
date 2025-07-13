import streamlit as st

def run():
    st.header("BRRRR Deal Analyzer")

    key_prefix = "brrrr_"

    # Section: Purchase & Rehab
    purchase_price = st.number_input("Purchase Price ($)", value=100000, key=f"{key_prefix}purchase_price")
    rehab_costs = st.number_input("Rehab Costs ($)", value=25000, key=f"{key_prefix}rehab_costs")
    closing_costs = st.number_input("Closing Costs ($)", value=5000, key=f"{key_prefix}closing_costs")
    holding_costs = st.number_input("Holding Costs ($)", value=3000, key=f"{key_prefix}holding_costs")

    total_investment = purchase_price + rehab_costs + closing_costs + holding_costs
    st.metric("Total Cash Invested", f"${total_investment:,.2f}")

    # Section: After Repair Value (ARV) & Refinance
    arv = st.number_input("After Repair Value (ARV) ($)", value=160000, key=f"{key_prefix}arv")
    refinance_ltv = st.slider("Refinance LTV (%)", min_value=50, max_value=100, value=75, key=f"{key_prefix}ltv")

    loan_amount = arv * (refinance_ltv / 100)
    cash_out = loan_amount - total_investment
    st.metric("Refinance Loan Amount", f"${loan_amount:,.2f}")
    st.metric("Cash Out / Left In Deal", f"${cash_out:,.2f}")

    # Section: Monthly Income & Expenses
    rent = st.number_input("Monthly Rent ($)", value=1500, key=f"{key_prefix}rent")
    mortgage_payment = st.number_input("Monthly Mortgage Payment ($)", value=800, key=f"{key_prefix}mortgage")
    taxes = st.number_input("Monthly Taxes ($)", value=150, key=f"{key_prefix}taxes")
    insurance = st.number_input("Monthly Insurance ($)", value=100, key=f"{key_prefix}insurance")
    property_management = st.number_input("Property Management (% of Rent)", value=8.0, step=0.1, key=f"{key_prefix}management_pct")

    management_fee = rent * (property_management / 100)
    total_expenses = mortgage_payment + taxes + insurance + management_fee
    cash_flow = rent - total_expenses

    st.metric("Monthly Cash Flow", f"${cash_flow:,.2f}")

    # Section: Cash-on-Cash Return
    if total_investment > 0:
        coc_return = (cash_flow * 12) / total_investment * 100
        st.metric("Cash-on-Cash Return", f"{coc_return:.2f}%")
    else:
        st.warning("Total investment is 0 — cannot compute return.")
