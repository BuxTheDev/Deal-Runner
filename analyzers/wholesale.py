import streamlit as st

def run():
    st.title("Wholesale Deal Analyzer")
    key_prefix = "wholesale_"
    # --- Deal Info ---
    st.header("Property Basics")
    arv = st.number_input("After Repair Value (ARV) ($)", value=200000)
    rehab_costs = st.number_input("Estimated Rehab Costs ($)", value=30000)
    investor_discount = st.slider("Investor Discount (% of ARV)", 50, 85, 70)

    # --- Your Deal ---
    st.header("Your Numbers")
    wholesale_fee = st.number_input("Your Desired Assignment Fee ($)", value=10000)
    closing_costs = st.number_input("Your Estimated Closing Costs ($)", value=3000)

    # --- Calculations ---
    # MAO: What your cash buyer is willing to pay
    mao = arv * (investor_discount / 100) - rehab_costs - closing_costs

    # Recommended offer = MAO - your fee
    recommended_offer = mao - wholesale_fee

    # Spread = MAO - Recommended offer (should match fee if done right)
    profit_spread = mao - recommended_offer

    # --- Output ---
    st.header("Results")
    st.metric("Maximum Allowable Offer (MAO)", f"${mao:,.2f}")
    st.metric("Recommended Offer to Seller", f"${recommended_offer:,.2f}")
    st.metric("Your Potential Profit", f"${profit_spread:,.2f}")

    with st.expander("Deal Breakdown"):
        st.write(f"ARV: ${arv:,.2f}")
        st.write(f"Rehab Costs: ${rehab_costs:,.2f}")
        st.write(f"Investor Discount: {investor_discount}% of ARV")
        st.write(f"Assignment Fee: ${wholesale_fee:,.2f}")
        st.write(f"Closing Costs: ${closing_costs:,.2f}")

if __name__ == "__main__":
    run()