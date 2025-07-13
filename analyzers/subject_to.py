import streamlit as st

def run():
    st.title("Subject-To Deal Analyzer")

    # --- Seller's Existing Mortgage ---
    st.header("Seller's Existing Mortgage")
    existing_loan_balance = st.number_input("Remaining Mortgage Balance ($)", value=220000)
    seller_monthly_payment = st.number_input("Monthly Mortgage Payment ($)", value=1300)
    years_left = st.number_input("Years Left on Loan", value=25)

    # --- Rental Income & Expenses ---
    st.header("Income & Expenses")
    monthly_rent = st.number_input("Monthly Rent Income ($)", value=2000)
    taxes = st.number_input("Monthly Taxes ($)", value=200)
    insurance = st.number_input("Monthly Insurance ($)", value=100)
    repairs_percent = st.slider("Repairs (% of rent)", 0, 20, 5)
    mgmt_percent = st.slider("Property Management (% of rent)", 0, 20, 8)
    vacancy_percent = st.slider("Vacancy (% of rent)", 0, 20, 5)

    # --- Upfront Costs & Seller Terms ---
    st.header("Upfront Investment")
    seller_carry = st.number_input("Seller Carry / 2nd Position ($)", value=0)
    repair_costs = st.number_input("Estimated Repairs ($)", value=10000)
    closing_costs = st.number_input("Estimated Closing Costs ($)", value=3000)
    assignment_fee = st.number_input("Your Assignment or Entry Fee ($)", value=5000)

    # --- Calculations ---
    repairs = monthly_rent * (repairs_percent / 100)
    mgmt = monthly_rent * (mgmt_percent / 100)
    vacancy = monthly_rent * (vacancy_percent / 100)

    # Total expenses = existing mortgage + monthly expenses
    total_expenses = seller_monthly_payment + taxes + insurance + repairs + mgmt + vacancy
    cash_flow = monthly_rent - total_expenses
    annual_cash_flow = cash_flow * 12

    # Total cash to close = any fees you pay upfront
    total_cash_invested = seller_carry + repair_costs + closing_costs + assignment_fee

    # ROI calculation
    if total_cash_invested > 0:
        cash_on_cash = (annual_cash_flow / total_cash_invested) * 100
    else:
        cash_on_cash = 0

    # Estimate equity captured
    purchase_equity = monthly_rent * 12 * years_left - (total_cash_invested + existing_loan_balance)

    # --- Output ---
    st.header("Results")
    st.metric("Monthly Cash Flow", f"${cash_flow:,.2f}")
    st.metric("Cash to Close", f"${total_cash_invested:,.2f}")
    st.metric("Cash-on-Cash Return", f"{cash_on_cash:.2f}%")

    with st.expander("Deal Summary"):
        st.write(f"Mortgage Balance: ${existing_loan_balance:,.2f}")
        st.write(f"Repairs: ${repair_costs:,.2f}")
        st.write(f"Closing Costs: ${closing_costs:,.2f}")
        st.write(f"Assignment Fee: ${assignment_fee:,.2f}")
        st.write(f"Seller Carry (2nd lien): ${seller_carry:,.2f}")
        st.write(f"Total Cash In: ${total_cash_invested:,.2f}")
        st.write("---")
        st.write(f"Management: ${mgmt:.2f}")
        st.write(f"Repairs: ${repairs:.2f}")
        st.write(f"Vacancy: ${vacancy:.2f}")
        st.write(f"Mortgage Payment: ${seller_monthly_payment:.2f}")
        st.write(f"Estimated Equity Gained Over Term: ${purchase_equity:,.2f}")
