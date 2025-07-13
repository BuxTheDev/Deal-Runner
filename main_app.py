import streamlit as st
from utils.constants import LAYOUT
from analyzers import rental, morby_method, brrrr, subject_to, wholesale, rental, fix_and_flip,mtr,

st.set_page_config(
    page_title="🏁 Deal Runner",
    layout=LAYOUT
)

# -----------------------------
# 🖼 Hero Banner
# -----------------------------
st.image("assets/deal_runner_banner.jepg", use_column_width=True)

st.markdown(
    "<h1 style='text-align: center; color: #FF3C00; font-family:monospace;'>DEAL RUNNER</h1>"
    "<p style='text-align: center; color: #AAAAAA;'>Run Real Estate Deals Like a Machine</p>",
    unsafe_allow_html=True
)

# -----------------------------
# Tabs Navigation
# -----------------------------
tabs = st.tabs([
    "Rental Deal Analyzer",
    "Morby Method Analyzer",
    "Brrr Method Analyzer",
    "Subject To Analyzer",
    "Wholesale Deal Analyzer",
    "rental Analyzer",
    "Fix and Flip Analyzer",
    "MTR Analyzer"
])

with tabs[0]:
    rental.run()
with tabs[1]:
    morby_method.run()
with tabs[2]:
    brrrr.run()
with tabs[3]:
    subject_to.run()
with tabs[4]:
    wholesale.run()
with tabs[5]:
    rental.run()
with tabs[6]:
    fix_and_flip.run()
with tabs[7]:
    mtr.run()

