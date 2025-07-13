import streamlit as st
from utils.ui import styled_analyzer_title  # make sure path is correct

# Page setup
st.set_page_config(page_title="Deal Runner", layout="centered")

# Custom Title
styled_analyzer_title("Deal Runner")

# Optional dropdown to load analyzer
analyzer_choice = st.selectbox(
    "Choose an Analyzer:",
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
