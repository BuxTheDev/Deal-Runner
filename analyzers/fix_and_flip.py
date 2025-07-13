import streamlit as st

def run():
    st.header("Fix & Flip Deal Analyzer")

    key_prefix = "flip_"

    # Section: Purchase & Rehab
    purchase_price = st.number_input("Purchase Price ($)", value=120000, key=f"{key_prefix}purchase_price")
    rehab_costs = st.number_input("Rehab Costs ($)", value=30000, key=f"{key_prefix}rehab_costs")
    closing_costs = st.number_input("Closing Costs ($)", value=6000, key=f"{key_prefix}closing_costs")
    holding_costs = st.number_input("Holding Costs ($)", value=4000, key=f"{key_prefix}holding_costs")
    selling_costs = st.number_input("Selling Costs (% of ARV)", value=8.0, step=0.1, key=f"{key_prefix}selling_costs_pct")

    total_investment = purchase_price + rehab_costs + closing_costs + holding_costs
    st.metric("Total Project Cost", f"${total_investment:,.2f}")

    # Section: Sale
    arv = st.number_input("After Repair Value (ARV) ($)", value=200000, key=f"{key_prefix}arv")
    estimated_selling_costs = arv * (selling_costs / 100)
    net_sale_proceeds = arv - estimated_selling_costs

    st.metric("Estimated Selling Costs", f"${estimated_selling_costs:,.2f}")
    st.metric("Net Sale Proceeds", f"${net_sale_proceeds:,.2f}")

    # Profit
    profit = net_sale_proceeds - total_investment
    roi = (profit / total_investment * 100) if total_investment > 0 else 0

    st.metric("Estimated Profit", f"${profit:,.2f}")
    st.metric("Return on Investment (ROI)", f"{roi:.2f}%")

    if profit < 0:
        st.warning("This deal is projected to lose money. Adjust your numbers.")
