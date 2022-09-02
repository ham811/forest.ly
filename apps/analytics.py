import streamlit as st
import leafmap.foliumap as leafmap

def app():

    st.title("Analyitics")
    with st.expander("See source code"):
        with st.echo():
            m = leafmap.Map()
            m.split_map(
                left_layer='Global Aboveground and Belowground Biomass Carbon Density Maps', right_layer='ESA WorldCover 2020'
            )
            m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

    m.to_streamlit(height=700)