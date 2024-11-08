# Import libraries
import streamlit as st
import pandas as pd
import altair as alt

import sys
import os

from snowflake.snowpark import Session


# To run streamlit: streamlit run c:/Users/kvoig/Documents/GitHub/oura_connector/app_contents/app.py




# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import settings
import settings

# Access the variable you need
connection_parameters = settings.connection_parameters

# Create a Snowpark session
session = Session.builder.configs(connection_parameters).create()

# Create a Snowpark DataFrame
snow_df = session.table("OURA_SLEEP")

# Convert Snowpark DataFrame to Pandas DataFrame
df = snow_df.to_pandas()

# Create the scatter chart
st.title("Scatter Chart Example")

chart = alt.Chart(df).mark_circle().encode(
    x='day:T',
    y='average_hrv:Q'
)

st.altair_chart(chart, use_container_width=True)

session.close()

