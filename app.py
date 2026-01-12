import streamlit as st
import pandas as pd

st.title("📈 Real-Time Product Price Tracker")

try:
    df = pd.read_csv("prices.csv")
    df["date"] = pd.to_datetime(df["date"])

    st.line_chart(df.set_index("date")["price"])

    st.write("### Price History")
    st.dataframe(df)

except FileNotFoundError:
    st.warning("No price data found. Run scraper.py first.")
