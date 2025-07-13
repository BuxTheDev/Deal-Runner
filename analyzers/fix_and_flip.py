import streamlit as st

def run():
    st.title("Fix & Flip Deal Analyzer")

    # --- Purchase & Rehab Info ---
    st.header("Purchase & Renovation")
    purchase_price = st.number_input("Purchase Price ($)", value=150000)
    rehab_costs = st.number_input("Rehab Costs ($)", value=40000)
    holding_costs = st.number_input("Holding Costs ($)", value=8000)
    timeline_months = st.number_input("Holding Time (Months)", value=6)

    # --- Exit Strategy ---
    st.header("Exit / Sale")
    arv = st.number_input("After Repair Value (ARV) ($)", value=250000)
    agent_commission_percent = st.slider("Agent Commission (%)", 0, 10, 6)
    closing_cost_percent = st.slider("Closing Costs (%)", 0, 10, 2)
    misc_costs = st.number_input("Other Selling Costs ($)", value=1000)

    # --- Calculations ---
    total_investment = purchase_price + rehab_costs + holding_costs

    # Commissions & sale expenses
    agent_commission = arv * (agent_commission_percent / 100)
    closing_costs = arv * (closing_cost_percent / 100)
    total_selling_costs = agent_commission + closing_costs + misc_costs

    # Net profit = ARV - (all costs)
    profit = arv - (total_investment + total_selling_costs)

    # ROI = profit / investment
    roi = (profit / total_investment) * 100 if total_investment > 0 else 0

    # Optional: average cost per month
    monthly_burn = total_investment / timeline_months if timeline_months > 0 else 0

    # --- Output ---
    st.header("Results")
    st.metric("Total Investment", f"${total_investment:,.2f}")
    st.metric("Total Profit", f"${profit:,.2f}")
    st.metric("ROI", f"{roi:.2f}%")

    with st.expander("Expense Breakdown"):
        st.write(f"Purchase Price: ${purchase_price:,.2f}")
        st.write(f"Rehab Costs: ${rehab_costs:,.2f}")
        st.write(f"Holding Costs: ${holding_costs:,.2f}")
        st.write("---")
        st.write(f"Agent Commission: ${agent_commission:,.2f}")
        st.write(f"Closing Costs: ${closing_costs:,.2f}")
        st.write(f"Misc Selling Costs: ${misc_costs:,.2f}")
        st.write("---")
        st.write(f"Monthly Burn Rate: ${monthly_burn:,.2f}")

if __name__ == "__main__":
    run()