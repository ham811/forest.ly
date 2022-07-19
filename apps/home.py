import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    This MorGis will utilize data
    analytics such as large-scale simulations and scenario
    analysis to inform decisions such as region/county
    selection, agricultural value chains and technology
    prioritization.

    Plenty dataset and accessible analysis for geospatial object information based on freely available satellite imagery as well as
    high resolution commercial data.
    Using both [Google Earth Engine](https://earthengine.google.com/) and [USGS](https://www.usgs.gov/) available data. 
    To create a direct link between different Earth analytics, and their impact on other environmental processes.

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)


