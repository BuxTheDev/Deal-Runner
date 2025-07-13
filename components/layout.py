import streamlit as st

def show_app_header(title: str):
    st.markdown(f"# {title}")
    st.caption("Built with 💼 by Bryan Buksoontorn")

def footer():
    st.markdown("---")
    st.caption("🧠 Ultimate Deal Analyzer | Co-built by Bryan & AI")
