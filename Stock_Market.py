import streamlit as st
import yfinance as yf
import datetime
import pandas as pd

#ticker_symbol  = 'MSFT'
stock_name = st.text_input("Enter Stock Name","MSFT", key = "placeholder")

st.title("Stock Market Analysis")
ticker_data = yf.Ticker(stock_name)
st.write(f"We are viewing info for {stock_name}")

col1, col2, col3 = st.columns(3)
with col1:
    start_dt = st.date_input("Enter Start Date",datetime.date(2020,1,1))
    st.header("Volume Analysis")

with col2:
    end_dt = st.date_input("Enter Start Date",datetime.date(2020, 12, 31))
    st.header("Closing Price Analysis")
with col3:
    st.header(" ")
    st.image("https://static.streamlit.io/examples/cat.jpg")
ticker_df = ticker_data.history(period = "14",
                                start = f"{start_dt}",
                                end = f"{end_dt}")

with col1:
    st.line_chart(ticker_df['Volume'])
with col2:
    st.line_chart(ticker_df['Close'])
st.header("DATA")
st.dataframe(ticker_df)
