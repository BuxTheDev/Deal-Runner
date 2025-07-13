import streamlit as st

def run():
    st.title("BRRRR Deal Analyzer")
     # --- Purchase and Rehab ---
    st.header("Buy & Rehab")
    purchase_price = st.number_input("Purchase Price ($)", value=150000)
    rehab_cost = st.number_input("Rehab Cost ($)", value=30000)
    holding_costs = st.number_input("Holding Costs ($)", value=5000)

    # --- after repair value and refinance ---
    st.header("Refinance Details")
    arv = st.number_input("After Repair Value (ARV) ($)", value=240000)
    refinance_percent = st.slider("Refinance Loan % of ARV", 50, 100, 75)
    refi_rate = st.number_input("Refi Interest Rate (%)", value=6.5)
    refi_term_years = st.number_input("Refi Loan Term (Years)", value=30)

     # --- Income & Expenses ---
    st.header("Rental Income & Expenses")
    monthly_rent = st.number_input("Monthly Rent ($)", value=1800)
    taxes = st.number_input("Monthly Taxes ($)", value=200)
    insurance = st.number_input("Monthly Insurance ($)", value=100)
    repairs_percent = st.slider("Repairs (% of rent)", 0, 20, 5)
    mgmt_percent = st.slider("Property Management (% of rent)", 0, 20, 8)
    vacancy_percent = st.slider("Vacancy (% of rent)", 0, 20, 5)

    # --- calculations below ---
    # total momey invested into the deal
    total_cash_in = purchase_price + rehab_cost + holding_costs

    # refi loan based on ARV
    refi_amount = arv * (refinance_percent / 100)

    # mortgage deets
    monthly_rate = (refi_rate / 100) / 12
    total_payments = refi_term_years * 12

    if monthly_rate > 0:
        mortgage_payment = refi_amount * (monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)
    else:
        mortgage_payment = refi_amount * total_payments

    # monthly expenses from rent
    repairs = monthly_rent * (repairs_percent / 100)
    mgmt = monthly_rent * (mgmt_percent / 100)
    vacancy = monthly_rent * (vacancy_percent / 100)
    total_expenses = taxes + insurance + repairs + mgmt + vacancy + mortgage_payment

    # cash flow
    cash_flow = monthly_rent - total_expenses
    annual_cash_flow = cash_flow * 12

    # cash pulled out or left in 
    equity_left_in = total_cash_in - refi_amount
    if equity_left_in < 0:
        cash_out = abs(equity_left_in)
        equity_left_in = 0
    else:
        cash_out = 0

    # ROI calculation
    cash_in = max(total_cash_in - refi_amount, 0)
    if cash_in > 0:
        cash_on_cash = (annual_cash_flow / cash_in) * 100
    else:
        cash_on_cash = 0

    # --- Output ---
    st.header("Results")
    st.metric("Refinance Amount", f"${refi_amount:,.2f}")
    st.metric("Mortgage Payment", f"${mortgage_payment:,.2f}")
    st.metric("Monthly Cash Flow", f"${cash_flow:,.2f}")
    st.metric("Cash-on-Cash Return", f"{cash_on_cash:.2f}%")

    with st.expander("Deal Breakdown"):
        st.write(f"Total Cash Invested: ${total_cash_in:,.2f}")
        st.write(f"Refi Loan: ${refi_amount:,.2f}")
        st.write(f"Equity Left In: ${equity_left_in:,.2f}")
        st.write(f"Cash Pulled Out: ${cash_out:,.2f}")
        st.write(f"Repairs: ${repairs:.2f}")
        st.write(f"Management: ${mgmt:.2f}")
        st.write(f"Vacancy: ${vacancy:.2f}")
        st.write(f"Taxes: ${taxes:.2f}")
        st.write(f"Insurance: ${insurance:.2f}")

if __name__ == "__main__":
    run()
