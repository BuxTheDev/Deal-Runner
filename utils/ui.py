import streamlit as st
import base64

def orange_header(text):
    st.markdown(f'<div class="orange-subheader">{text}</div>', unsafe_allow_html=True)

def orange_title(text):
    st.markdown(f"""
        <h1 style="color:#ff8800;
                   font-size:2.2rem;
                   text-align:center;
                   margin-top:0;">
            {text}
        </h1>
    """, unsafe_allow_html=True)

def load_custom_font():
    with open("assets\\deal_runner.ttf", "rb") as f:
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
                text-align: center;
            }}
        </style>
    """, unsafe_allow_html=True)

def styled_analyzer_title(text):
    load_custom_font()
    st.markdown(f'<div class="deal-analyzer-title">{text}</div>', unsafe_allow_html=True)

def styled_selectbox(label: str, options: list, key: str = None):
    st.markdown(f"""
        <style>
        /* Target Streamlit dropdown by its internal CSS structure */
        div[data-baseweb="select"] > div {{
            justify-content: center;
        }}

        /* Selected value text */
        div[data-baseweb="select"] span {{
            color: #ff8800 !important;
            font-weight: 700 !important;
            text-align: center !important;
        }}

        /* Optional: tweak the whole dropdown box */
        div[data-baseweb="select"] {{
            padding: 5px 8px;
            font-size: 1.05rem;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Wrap it in a container so it's centered on the page
    with st.container():
        st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
        selection = st.selectbox(label, options, key=key, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    return selection
