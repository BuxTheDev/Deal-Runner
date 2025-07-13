import streamlit as st
from utils.constants import LAYOUT
from analyzers import rental, morby_method, brrrr

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="🏡 Ultimate Deal Analyzer",
    layout=LAYOUT
)

# ---------------------------------------
# App Title
# ---------------------------------------
st.title("🏡 Ultimate Deal Analyzer")

# ---------------------------------------
# Tabs for Each Deal Calculator
# ---------------------------------------
tabs = st.tabs([
    "Rental Deal Analyzer",
    "Morby Method Analyzer",
    "Brrrr (test)" #FIXME
])

# ---------------------------------------
# Calculator Routing by Tab
# ---------------------------------------
with tabs[0]:
    rental.run()

with tabs[1]:
    morby_method.run()

with tabs[2]:
    brrrr.run()
