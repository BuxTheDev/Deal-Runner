import streamlit as st

# Set centered layout
st.set_page_config(page_title="Deal Runner", layout="centered")

# Inject custom CSS for styling
st.markdown("""
    <style>
        .big-label {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .orange-subheader {
            font-size: 1.1rem !important;
            color: #ff8800 !important;
            font-weight: 600;
            margin-top: 1.5rem;
        }

        .stSelectbox label {
            font-size: 1.3rem;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("Deal Runner")

# Custom dropdown label
st.markdown('<div class="big-label">Select a Deal Analyzer:</div>', unsafe_allow_html=True)

# Analyzer dropdown (no STR)
analyzer_choice = st.selectbox(
    "",
    [
        "Rental Analyzer",
        "Morby Method Analyzer",
        "BRRRR Analyzer",
        "Subject-To Analyzer",
        "Wholesale Analyzer",
        "Fix & Flip Analyzer",
        "MTR Analyzer"
    ]
)

# Load selected analyzer
if analyzer_choice == "Rental Analyzer":
    import analyzers.rental as rental
    rental.run()
elif analyzer_choice == "Morby Method Analyzer":
    import analyzers.morby_method as morby
    morby.run()
elif analyzer_choice == "BRRRR Analyzer":
    import analyzers.brrrr as brrrr
    brrrr.run()
elif analyzer_choice == "Subject-To Analyzer":
    import analyzers.subject_to as subject_to
    subject_to.run()
elif analyzer_choice == "Wholesale Analyzer":
    import analyzers.wholesale as wholesale
    wholesale.run()
elif analyzer_choice == "Fix & Flip Analyzer":
    import analyzers.fix_and_flip as flip
    flip.run()
elif analyzer_choice == "MTR Analyzer":
    import analyzers.mtr as mtr
    mtr.run()
