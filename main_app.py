import streamlit as st

# Set centered layout (if not already set elsewhere)
st.set_page_config(page_title="Deal Runner", layout="centered")

st.title("🏡 Deal Runner - Choose Your Analyzer")

# Create button grid
col1, col2, col3, col4 = st.columns(4)

analyzer_selected = None

with col1:
    if st.button("Rental"):
        analyzer_selected = "rental"
with col2:
    if st.button("Morby Method"):
        analyzer_selected = "morby"
with col3:
    if st.button("BRRRR"):
        analyzer_selected = "brrrr"
with col4:
    if st.button("Subject-To"):
        analyzer_selected = "subject_to"

col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("Wholesale"):
        analyzer_selected = "wholesale"
with col6:
    if st.button("MTR"):
        analyzer_selected = "mtr"
with col7:
    if st.button("Fix & Flip"):
        analyzer_selected = "flip"


st.markdown("---")

# Show the selected analyzer
if analyzer_selected == "rental":
    import analyzers.rental as rental
    rental.run()
elif analyzer_selected == "morby":
    import analyzers.morby_method as morby
    morby.run()
elif analyzer_selected == "brrrr":
    import analyzers.brrrr as brrrr
    brrrr.run()
elif analyzer_selected == "subject_to":
    import analyzers.subject_to as subject_to
    subject_to.run()
elif analyzer_selected == "wholesale":
    import analyzers.wholesale as wholesale
    wholesale.run()
elif analyzer_selected == "mtr":
    import analyzers.mtr as mtr
    mtr.run()
elif analyzer_selected == "flip":
    import analyzers.fix_and_flip as flip
    flip.run()

