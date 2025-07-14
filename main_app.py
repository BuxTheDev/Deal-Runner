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

# Load the selected analyzer module and run it
if selected == "Morby Method Analyzer":
    import analyzers.morby_method as morby
    morby.run()
elif selected == "Rental Deal Analyzer":
    import analyzers.rental as rental
    rental.run()
elif selected == "BRRRR Deal Analyzer":
    import analyzers.brrrr as brrrr
    brrrr.run()
elif selected == "Fix and Flip":
    import analyzers.fix_and_flip as fix_and_flip
    fix_and_flip.run()