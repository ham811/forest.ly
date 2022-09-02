import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_agg import RendererAgg


#Loading the data
@st.cache
def get_data_deputies():
     return pd.read_csv(os.path.join(os.getcwd(),'precip_berlin.csv'))



def app():
    #configuration of the page
    st.set_page_config(layout="wide")
    #load dataframes
    df_dep = get_data_deputies()
    st.title('Patches vizualisation tool')
    st.markdown("""
    This app performs simple visualization from the Forest Patches Features!
    """)
    st.write(df_dep)


    st.sidebar.header('Select what to display')
    pol_parties = df_dep['Year'].unique().tolist()
    pol_party_selected = st.sidebar.multiselect('Political parties', pol_parties, pol_parties)
    nb_deputies = df_dep['Month'].value_counts()
    nb_mbrs = st.sidebar.slider("Number of members", int(nb_deputies.min()), int(nb_deputies.max()), (int(nb_deputies.min()), int(nb_deputies.max())), 1)
    #creates masks from the sidebar selection widgets
    mask_pol_par = df_dep['Month'].isin(pol_party_selected)
    #get the parties with a number of members in the range of nb_mbrs
    mask_mbrs = df_dep['Month'].value_counts().between(nb_mbrs[0], nb_mbrs[1]).to_frame()
    mask_mbrs= mask_mbrs[mask_mbrs['Month'] == 1].index.to_list()
    mask_mbrs= df_dep['Month'].isin(mask_mbrs)

    df_dep_filtered = df_dep[mask_pol_par & mask_mbrs]
    st.write(df_dep_filtered)   