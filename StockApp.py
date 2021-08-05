# description : this is a stock market dashboard that I have been researching to show the charts and data

# Import the lib
from typing import Any, Union

import streamlit as st
import pandas as pd
import yfinance as yf
from PIL import Image



# adding title and image
from pandas import Series, DataFrame
from pandas.core.generic import NDFrame
from pandas.io.parsers import TextFileReader

st.write("""
# Stock Market Web Application
**Visually** show data on stock by Sanjida Firdaws, Data range from Feb 3, 2020 - June 30, 2020
""")

image = Image.open("C:/Users/sanji/PycharmProjects/pythonProject/stock-exchanges.jpg")
st.image(image, use_column_width=True)

# create a sidebar header
st.sidebar.header('User Input')
#data = yf.download("FB NELX FOX TMUS VZ", start="2020-02-01", end="2020-06-30")

# create a function to get users input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-02-03")
    end_date = st.sidebar.text_input("End Date", "2020-06-29")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "FB")
    return start_date, end_date, stock_symbol


# create a function to get the company name
def get_company_name(symbol):
    if symbol == 'FB':
        return 'FaceBook'
    elif symbol == 'NELX':
        return 'Netflix'
    elif symbol == 'FOX':
        return 'FOX'
    elif symbol == 'TMUS':
        return 'T-Mobile'
    elif symbol == 'VZ':
        return 'Verizon'
    else:
        'None'

# create a function to get the proper company data and the proper timeframe from the user start dat to teh end date
def get_data(symbol, start, end):
    return ( yf.download( tickers = symbol, start = start, end = end ))

# get the users input
start, end, symbol = get_input()    # add statement for specific date formatting needed: YYYY-MM-DD
# get the data
df = get_data(symbol, start, end)
# get the company name
company_name = get_company_name(symbol.upper())

# display the close price
st.header(company_name+ " Close Price \n")
st.line_chart(df['Close'])

# display the volume price
st.header(company_name+ " Volume \n")
st.line_chart(df['Volume'])

# get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
