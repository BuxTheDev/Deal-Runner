import streamlit as st

def section_header(title: str):
    st.markdown(f"### {title}")

def labeled_number_input(
    label: str,
    min_value: float = 0.0,
    max_value: float = None,
    value: float = 0.0,
    step: float = 0.01,
    number_format: str = "%.2f",
    key: str = None
) -> float:
    return st.number_input(
        label,
        min_value=min_value,
        max_value=max_value,
        value=value,
        step=step,
        format=number_format,
        key=key
    )

def currency_input(label: str, value: float = 0.0, key: str = None) -> float:
    return labeled_number_input(
        label=f"{label} ($)",
        value=float(value),
        step=100.0,
        number_format="%.2f",
        key=key
    )

def percent_input(label: str, value: float = 0.0, key: str = None) -> float:
    return labeled_number_input(
        label=f"{label} (%)",
        value=value,
        step=0.1,
        number_format="%.1f",
        key=key
    )

def two_column_inputs(input_list: list) -> list:
    """
    Accepts a list of tuples: (label, kwargs_dict)
    Returns list of input values.
    Example:
        inputs = [
            ("Purchase Price", {"value": 200000}),
            ("Down Payment", {"value": 40000}),
        ]
    """
    cols = st.columns(2)
    values = []
    for i, (label, kwargs) in enumerate(input_list):
        with cols[i % 2]:
            value = labeled_number_input(label, **kwargs)
            values.append(value)
    return values
