import streamlit as st

# Set centered layout
st.set_page_config(page_title="Deal Runner", layout="centered")

st.title("🏡 Deal Runner")

# Analyzer Selection Dropdown
analyzer_choice = st.selectbox(
    "Select an Analyzer:",
    [
        "Rental Analyzer",
        "Morby Method Analyzer",
        "BRRRR Analyzer",
        "Subject-To Analyzer",
        "Wholesale Analyzer",
        "Fix & Flip Analyzer",
        "MTR Analyzer",
        # Add more analyzers here as needed
    ]
)

# Render the selected analyzer
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
