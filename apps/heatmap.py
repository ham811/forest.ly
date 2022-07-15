import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Population Heatmap")

    filepath = "https://raw.githubusercontent.com/ham811/streamli_app/main/data/ma.csv"
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
        filepath,
        latitude="lat",
        longitude="lng",
        value="population",
        name="Heatmap",
        radius=20,
    )
    m.to_streamlit(height=700)
