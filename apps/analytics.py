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
    
    df = "https://raw.githubusercontent.com/ham811/forest.ly/main/data/precip_berlin.csv"

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Year', 'Month', 'Mitte', 'Moabit'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
    st.line_chart(df)

    return pd.read_csv(df)
    
    