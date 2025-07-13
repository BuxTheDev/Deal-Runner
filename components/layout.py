import streamlit as st

def show_app_header(title: str):
    st.markdown(f"# {title}")
    st.caption("Built with 💼 by Bryan Buksoontorn")

def footer():
    st.markdown("---")
    st.caption("🧠 Ultimate Deal Analyzer | Co-built by Bryan & AI")

def section_header(icon: str, title: str):
    st.markdown(f"### {icon} {title}")

def two_column_inputs(left_inputs: list, right_inputs: list):
    col1, col2 = st.columns(2)
    with col1:
        for input_func in left_inputs:
            input_func()
    with col2:
        for input_func in right_inputs:
            input_func()


def three_column_metrics(metrics: list):
    # Split metrics into rows of 3
    for i in range(0, len(metrics), 3):
        row = metrics[i:i+3]
        cols = st.columns(len(row))
        for col, (label, value) in zip(cols, row):
            with col:
                st.metric(label, value)


def horizontal_rule():
    st.markdown("<hr style='border: 0.5px solid #EEE;'>", unsafe_allow_html=True)
