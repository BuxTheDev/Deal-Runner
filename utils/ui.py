import streamlit as st

def orange_header(text):
    st.markdown(f'<div class="orange-subheader">{text}</div>', unsafe_allow_html=True)

def orange_title(text):
    st.markdown(f'<h1 style="color:#ff8800; font-size:2.2rem;">{text}</h1>', unsafe_allow_html=True)