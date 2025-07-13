import streamlit as st
from utils.ui import orange_header

def run():
    key_prefix = "rental_"
    orange_header("Rental Deal Analyzer")
    # the following values are just examples for the user
    purchase_price = st.number_input("Purchase Price ($)", value=250000)
    down_payment_percent = st.slider("Down Payment (%)", 0, 100, 20) #let user pick down payment percentage using a slider
    interest_rate = st.number_input("Interest Rate (%)", value=6.5)
    loan_term_years = st.number_input("Loan Term (years)", value=30)
    monthly_rent = st.number_input("Monthly Rent ($)", value=1800)
    taxes = st.number_input("Monthly Property Taxes ($)", value=250)
    insurance = st.number_input("Monthly Insurance ($)", value=100)
    repairs_percent = st.slider("Repairs (% of rent)", 0, 20, 5) # repair cost
    mgmt_percent = st.slider("Property Management (% of rent)", 0, 20, 8)
    vacancy_percent = st.slider("Vacancy (% of rent)", 0, 20, 5) # slider to account for vacancy as a % of rent

    # --- Calculations below ---

    down_payment = purchase_price * (down_payment_percent / 100) # how much $$$ is needed for dp 
    loan_amount = purchase_price - down_payment
    monthly_interest = (interest_rate / 100) / 12 # formula for monthly rate
    total_payments = loan_term_years * 12

    # --- Calculate the monthly mortgage payment using the amortization formula ---

    if monthly_interest > 0:
        monthly_mortgage = loan_amount * (monthly_interest * (1 + monthly_interest)**total_payments) / ((1 + monthly_interest)**total_payments - 1)
    else:
        # if interest is 0 then its just loan amount divided by months
        monthly_mortgage = loan_amount / total_payments

    gross_rent = monthly_rent # gross rent: total rent before expenses

    repairs = monthly_rent * (repairs_percent/100)
    mgmt = monthly_rent * (mgmt_percent / 100)
    vacancy = monthly_rent * (vacancy_percent / 100)

    total_expenses = monthly_mortgage + taxes + insurance + repairs + mgmt + vacancy
    cash_flow = gross_rent - total_expenses
    annual_cash_flow = cash_flow * 12

    # cash on cash return = how much you make per year / how much you invested (down payment)
    if down_payment > 0: 
        cash_on_cash = (annual_cash_flow / down_payment) * 100
    else:
        cash_on_cash = 0

    # --- Output Section --- 
    st.header("Results") #FIXME make prettier
    # Display the monthly mortgage payment
    st.metric("Monthly Mortgage", f"${monthly_mortgage:,.2f}")
    st.metric("Monthly Cash Flow", f"${cash_flow:,.2f}")
    st.metric("Cash-on-Cash Return", f"{cash_on_cash:.2f}%")

    with st.expander("Expense Breakdown"):
        st.write(f"Repairs: ${repairs:.2f}")
        st.write(f"Management: ${mgmt:.2f}")
        st.write(f"Vacancy: ${vacancy:.2f}")
        st.write(f"Taxes: ${taxes:.2f}")
        st.write(f"Insurance: ${insurance:.2f}")
        st.write(f"Mortgage: ${monthly_mortgage:.2f}")

if __name__ == "__main__":
    run()