import yfinance as yf 
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Apple!
""")

tickerSymbol = 'AAPL'

#get data from ticker 
tickerData = yf.Ticker(tickerSymbol)

#get the prices
tickerDf = tickerData.history(period = '1d', start = '2010-01-01', end = '2021-03-01')
#This creates a dataframe with the following columns { Open, High, Low, Close, Volume, Dividends, Splits}

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume 
""")
st.line_chart(tickerDf.Volume)

# Notes: 
# Streamlit uses markdown language syntax, a good reference which is below
# https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet