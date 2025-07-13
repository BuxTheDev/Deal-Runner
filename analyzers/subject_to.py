import streamlit as st

def run():
    st.header("Subject-To Deal Analyzer")

    # Prefix to keep keys unique
    key_prefix = "subject_to_"

    purchase_price = st.number_input("Purchase Price ($)", value=200000, key=f"{key_prefix}purchase_price")
    loan_balance = st.number_input("Existing Loan Balance ($)", value=180000, key=f"{key_prefix}loan_balance")
    monthly_piti = st.number_input("Monthly PITI ($)", value=1041, key=f"{key_prefix}monthly_piti")
    insurance = st.number_input("Monthly Insurance ($)", value=100, key=f"{key_prefix}insurance")
    taxes = st.number_input("Monthly Taxes ($)", value=150, key=f"{key_prefix}taxes")
    hoa = st.number_input("Monthly HOA ($)", value=0, key=f"{key_prefix}hoa")
    arv = st.number_input("After Repair Value (ARV) ($)", value=250000, key=f"{key_prefix}arv")
    est_rent = st.number_input("Estimated Monthly Rent ($)", value=1700, key=f"{key_prefix}rent")

    # Add logic or output summary here
    monthly_cashflow = est_rent - monthly_piti - hoa
    st.metric("Estimated Monthly Cash Flow", f"${monthly_cashflow:.2f}")
