"""This module contains the logic for the Streamlit app."""
import streamlit as st
from config import Analysis, dspy

Analysis_function = dspy.ChainOfThought(Analysis)


def main():
    """Main function for the Streamlit app."""
    st.title("Hydrological Analysis Tool")

    st.header("Input Parameters")
    location = st.text_input("Location for analysis", "Warangal, Telangana, India.")
    groundwater_level = st.text_input(
        "Groundwater level at the location", "6.4 - 8 ft below ground."
    )
    criticality = st.selectbox(
        "Criticality based on groundwater level", ["Low", "Moderate", "High"]
    )

    if st.button("Run Analysis"):
        analysis = Analysis_function(
            context="",
            location=location,
            groundwater_level=groundwater_level,
            criticality=criticality,
        )

        result = analysis

        st.header("Analysis Results")
        st.write(f"**Recommendations:** {result.recommendations}")
        st.write(f"**Potential Risks:** {result.potential_risks}")
        st.write(f"**Causes of Water Scarcity:** {result.causes_of_water_scarcity}")
        st.write(f"**Mitigation Measures:** {result.mitigation_measures}")


if __name__ == "__main__":
    main()
