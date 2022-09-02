import streamlit as st
import leafmap.foliumap as leafmap

def app():

    st.title("ESA LandCover")
    with st.expander("See source code"):
        with st.echo():
            m = leafmap.Map()
            m.split_map(
                left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
            )
            m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

    m.to_streamlit(height=700)