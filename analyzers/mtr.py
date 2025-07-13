import streamlit as st

def run():
    st.title("Mid-Term Rental (MTR) Analyzer")

    key_prefix = "mtr_"

    # --- Property & Loan Info ---
    st.header("Property Details")
    purchase_price = st.number_input("Purchase Price ($)", value=250000)
    down_payment_percent = st.slider("Down Payment (%)", 0, 100, 20)
    interest_rate = st.number_input("Loan Interest Rate (%)", value=6.5)
    loan_term_years = st.number_input("Loan Term (years)", value=30)

    # --- MTR Income ---
    st.header("Monthly MTR Rent")
    mtr_rent = st.number_input("Monthly Rent (Furnished)", value=2800)

    # --- Monthly Expenses ---
    st.header("Operating Expenses")
    cleaning = st.number_input("Cleaning Service ($/month)", value=150)
    wifi = st.number_input("WiFi ($/month)", value=75)
    utilities = st.number_input("Utilities ($/month)", value=200)
    taxes = st.number_input("Property Taxes ($/month)", value=250)
    insurance = st.number_input("Insurance ($/month)", value=100)
    repairs_percent = st.slider("Repairs (% of rent)", 0, 20, 5)
    mgmt_percent = st.slider("Property Management (% of rent)", 0, 20, 8)
    vacancy_percent = st.slider("Vacancy (% of rent)", 0, 20, 5)

    # --- Startup Costs ---
    st.header("Setup Costs")
    furnishing_costs = st.number_input("Furnishing & Setup ($)", value=10000)
    closing_costs = st.number_input("Closing Costs ($)", value=4000)

    # --- Calculations ---
    down_payment = purchase_price * (down_payment_percent / 100)
    loan_amount = purchase_price - down_payment
    monthly_interest = (interest_rate / 100) / 12
    total_payments = loan_term_years * 12

    if monthly_interest > 0:
        mortgage = loan_amount * (monthly_interest * (1 + monthly_interest)**total_payments) / ((1 + monthly_interest)**total_payments - 1)
    else:
        mortgage = loan_amount / total_payments

    repairs = mtr_rent * (repairs_percent / 100)
    mgmt = mtr_rent * (mgmt_percent / 100)
    vacancy = mtr_rent * (vacancy_percent / 100)

    total_monthly_expenses = mortgage + taxes + insurance + repairs + mgmt + vacancy + cleaning + wifi + utilities
    monthly_cash_flow = mtr_rent - total_monthly_expenses
    annual_cash_flow = monthly_cash_flow * 12

    total_cash_invested = down_payment + closing_costs + furnishing_costs

    if total_cash_invested > 0:
        cash_on_cash = (annual_cash_flow / total_cash_invested) * 100
        payback_months = total_cash_invested / monthly_cash_flow if monthly_cash_flow > 0 else float("inf")
    else:
        cash_on_cash = 0
        payback_months = float("inf")

    # --- Output ---
    st.header("Results")
    st.metric("Monthly Cash Flow", f"${monthly_cash_flow:,.2f}")
    st.metric("Cash-on-Cash Return", f"{cash_on_cash:.2f}%")
    st.metric("Payback Period", f"{payback_months:.1f} months")
