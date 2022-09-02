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

dataset_url = "https://raw.githubusercontent.com/ham811/forest.ly/main/data/precip_berlin.csv"

# read csv from a URL
@st.experimental_memo
def app() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = app()