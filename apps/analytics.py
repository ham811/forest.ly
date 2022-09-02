# import streamlit as st 
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
# import os
# from matplotlib.backends.backend_agg import RendererAgg


# #Loading the data


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Create file uploader object
upload_file = 'https://raw.githubusercontent.com/ham811/forest.ly/main/data/precip_berlin.csv'

# Check to see if a file has been uploaded
if upload_file is not None:
    # If it has then do the following:

    # Read the file to a dataframe using pandas
    df = pd.read_csv(upload_file)

    # Create a section for the dataframe statistics
    st.header('Statistics of Dataframe')
    st.write(df.describe())

    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.write(df.head())

    # Create a section for matplotlib figure
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Year'], y=df['Month'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Value')
    
    st.pyplot(fig)

# # read csv from a URL
# @st.cache
# def app() -> pd.DataFrame:
    
#     df = "https://raw.githubusercontent.com/ham811/forest.ly/main/data/precip_berlin.csv"

#     # Pie chart, where the slices will be ordered and plotted counter-clockwise:
#     labels = 'Year', 'Month', 'Mitte', 'Moabit'
#     sizes = [15, 30, 45, 10]
#     explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

#     fig1, ax1 = plt.subplots()
#     ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#             shadow=True, startangle=90)
#     ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    

#     return pd.read_csv(df)

# st.pyplot()
# st.line_chart()
    