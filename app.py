import pandas as pd
import plotly.express as px
import streamlit as st

#Creates a website using streamlit which generates html/css/javascript code from this python code

#   INITIALIZE

st.set_page_config(layout="wide",
                   page_icon="⛽",
                   page_title="Fuel Economy Calculator")

# Makes it so everytime we change the filter on the data, it doesn't have to read the excel file again
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io = 'fuelEconomyData.xlsx',
        engine = 'openpyxl',
        sheet_name = 'Sheet1',
        usecols="A:D"
        )

    df["Fuel Economy"] = (df["Distance"] / df["Fuel"])
    return df
df = get_data_from_excel()

# SIDEBAR
#st.dataframe(df)
st.sidebar.header("Filter here:")
date = st.sidebar.multiselect(
    "Select Date:",
    options = df['Date'].unique(),
    default = df['Date'].unique()
)
df_selection = df.query("Date == @date")

#uncomment this to see the excel data in the website
#st.dataframe(df_selection)

# MAIN PAGE
st.title("⛽ Fuel Economy Calculator")
st.markdown("##")

# STATS
total_amount_spent = df_selection["Price"].mean() * df_selection["Fuel"].sum()
average_fuel_price = df_selection["Price"].mean()
average_litres_filled = df_selection["Fuel"].mean()
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Amount Spent:")
    st.subheader(f"AUD ${total_amount_spent:.2f}")
with middle_column:
    st.subheader("Average Fuel Price:")
    st.subheader(f"AUD ${average_fuel_price:.2f}")
with right_column:
    st.subheader("Average Amount Filled:")
    st.subheader(f"AUD ${average_litres_filled:.2f}")
    
st.markdown("---")

# GRAPHS

date = (
     df_selection.groupby(by=["Date"]).sum()[["Fuel Economy"]].sort_values(by="Fuel Economy")
)

figure_fuel_economy = px.bar(
    date,
    x = "Fuel Economy",
    y = date.index,
    orientation='h',
    title = "<b>Fuel Economy<b>",
    color_discrete_sequence=["#00cc96"] * len(date),
    template = "plotly_white",
)

st.plotly_chart(figure_fuel_economy, use_container_width=True)

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)