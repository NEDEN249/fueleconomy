import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide",
                   page_icon=":smiley:",
                   page_title="Fuel Economy Calculator")

df = pd.read_excel(
    io = 'fuelEconomyData.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Sheet1',
    skiprows=1,
    usecols="A:D"
    )

st.dataframe(df)