# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import statsmodels.api as sm
import sys
import os

from sqlalchemy import create_engine



# Title for the app
st.title("My Daily Readiness Score from Oura")



# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import settings
import settings

# Database credentials
server = settings.AZURE_SERVER_NAME
database = settings.AZURE_DATABASE_NAME
username = settings.AZURE_DATABASE_USERNAME
password = settings.AZURE_DATABASE_PASSWORD

# Connection string
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string)

def fetch_data(query):
    with engine.connect() as connection:
        return pd.read_sql(query, connection)


# Fetch data
query = """
        SELECT *
        FROM LANDING.OURA_DAILY_READINESS
        """

df = fetch_data(query)
df = pd.DataFrame(df)

# To run streamlit: streamlit run c:/Users/kvoig/Documents/GitHub/oura_connector/app_contents/app.py

df['day'] = pd.to_datetime(df['day'], format = "%Y-%m-%d")

# Create the scatter chart
st.title("Scatter Chart Example")

fig = px.scatter(df, x="day", y="score", trendline='lowess', trendline_color_override="red")

st.plotly_chart(fig)

# session.close()

