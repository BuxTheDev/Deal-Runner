import streamlit as st

def show_summary(title: str, results: dict):
    """
    Displays key deal results as Streamlit metrics.

    Parameters:
        title (str): Title of the summary section.
        results (dict): Dictionary with labels as keys and result values as strings/numbers.
    """
    st.markdown(f"## 📊 {title}")
    cols = st.columns(min(4, len(results)))

    for i, (label, value) in enumerate(results.items()):
        with cols[i % len(cols)]:
            st.metric(label=label, value=value)

def show_advanced_metrics(title: str, metrics: list):
    """
    Displays a longer list of metrics (e.g., full financial breakdown).

    Parameters:
        title (str): Section heading
        metrics (list): List of (label, value) tuples
    """
    st.markdown(f"### 📈 {title}")
    for label, value in metrics:
        st.write(f"**{label}:** {value}")

def show_alert(message: str, level: str = "info"):
    """
    Displays a Streamlit alert box.

    level: "info", "success", "warning", or "error"
    """
    if level == "info":
        st.info(message)
    elif level == "success":
        st.success(message)
    elif level == "warning":
        st.warning(message)
    elif level == "error":
        st.error(message)

