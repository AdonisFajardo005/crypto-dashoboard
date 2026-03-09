import streamlit as st
import plotly.express as px

from crypto_api import get_crypto_data
from analysis import moving_average, calculate_returns


st.title("Crypto Market Dashboard")

coin = st.selectbox(
    "Select Cryptocurrency",
    ["bitcoin", "ethereum", "solana", "cardano"]
)

days = st.slider(
    "Select days",
    7,
    90,
    30
)


df = get_crypto_data(coin, days)

df = moving_average(df)

df = calculate_returns(df)


st.subheader("Price Chart")

fig = px.line(
    df,
    x="timestamp",
    y=["price", "MA"],
    title=f"{coin} price analysis"
)

st.plotly_chart(fig)


st.subheader("Statistics")

st.write("Average price:", round(df["price"].mean(), 2))
st.write("Max price:", round(df["price"].max(), 2))
st.write("Min price:", round(df["price"].min(), 2))


st.subheader("Raw Data")

st.dataframe(df)