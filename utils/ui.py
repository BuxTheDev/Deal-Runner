import streamlit as st
import base64

def orange_header(text):
    st.markdown(f'<div class="orange-subheader">{text}</div>', unsafe_allow_html=True)

def orange_title(text):
    st.markdown(f'<h1 style="color:#ff8800; font-size:2.2rem;">{text}</h1>', unsafe_allow_html=True)

def load_custom_font():
    with open("assets\deal_runner.ttf", "rb") as f:
        font_data = f.read()
    font_base64 = base64.b64encode(font_data).decode()

    st.markdown(f"""
        <style>
            @font-face {{
                font-family: 'CustomFont';
                src: url(data:font/ttf;base64,{font_base64}) format('truetype');
            }}
            .deal-analyzer-title {{
                font-family: 'CustomFont', sans-serif;
                color: #ff8800;
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 1.5rem;
            }}
        </style>
    """, unsafe_allow_html=True)

def styled_analyzer_title(text):
    load_custom_font()
    st.markdown(f'<div class="deal-analyzer-title">{text}</div>', unsafe_allow_html=True)
