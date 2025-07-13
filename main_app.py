import streamlit as st
from analyzers import rental, morby_method, wholesale, brrrr, fix_and_flip, mtr, subject_to # Extend as you add more
from components.layout import show_app_header, footer

# App branding and config
st.set_page_config(
    page_title="Deal Runner",
    page_icon="🚀",
    layout="wide"
)

# Header
show_app_header("🚀 Deal Runner – Ultimate Real Estate Deal Analyzer")

# Sidebar menu
menu = st.sidebar.selectbox("📂 Choose a Calculator", [
    "🏠 Rental Deal Analyzer",
    "💵 Morby Method Analyzer",
    "📦 Wholesale Deal Analyzer",
    "🛠 BRRRR Analyzer",
    "🔨 Fix & Flip Analyzer",
    "📄 Subject-To Analyzer",
    "🛏️ Mid-Term Rental Analyzer"
])

# Route to analyzer modules
if menu == "🏠 Rental Deal Analyzer":
    rental.run()

elif menu == "💵 Morby Method Analyzer":
    morby_method.run()

elif menu == "📦 Wholesale Deal Analyzer":
    wholesale.run()

elif menu == "🛠 BRRRR Analyzer (Coming Soon)":
    brrrr.run()
    
elif menu == "🔨 Fix & Flip Analyzer":
    fix_and_flip.run()

elif menu == "📄 Subject-To Analyzer":
    subject_to.run()

elif menu == "🛏️ Mid-Term Rental Analyzer":
    mtr.run()

# Footer
footer()
