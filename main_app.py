import streamlit as st
import components.layout as layout
import utils.ui as ui

# Set page config
st.set_page_config(page_title="Deal Runner", layout="centered")

# Styled title at the top
ui.styled_analyzer_title("Deal Runner")

# Dropdown selector for analyzers
selected = layout.analyzer_selector([
    "Morby Method Analyzer",
    "Rental Deal Analyzer",
    "BRRRR Deal Analyzer",
    "Fix and Flip Analyzer",
    "Subject To Analyzer",
    "Wholesale Deal Analyzer",
    "MTR Analyzer"
])

# Load and run selected analyzer
if selected == "Morby Method Analyzer":
    import analyzers.morby_method as morby
    morby.run()
elif selected == "Rental Deal Analyzer":
    import analyzers.rental as rental
    rental.run()
elif selected == "BRRRR Deal Analyzer":
    import analyzers.brrrr as brrrr
    brrrr.run()
elif selected == "Fix and Flip Analyzer":
    import analyzers.fix_and_flip as flip
    flip.run()
elif selected == "Subject To Analyzer":
    import analyzers.subject_to as subject_to
    subject_to.run()
elif selected == "Wholesale Deal Analyzer":
    import analyzers.wholesale as wholesale
    wholesale.run()
elif selected == "MTR Analyzer":
    import analyzers.mtr as mtr
    mtr.run()
