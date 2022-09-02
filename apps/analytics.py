import streamlit as st 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_agg import RendererAgg


#Loading the data




# read csv from a URL
@st.cache
def app() -> pd.DataFrame:
    
    df = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

    st.line_chart(df)
    
    return pd.read_csv(df)
    
    