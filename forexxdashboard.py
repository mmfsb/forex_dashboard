import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

# Titles and subtitles
st.title('Forex Daily Prices')
st.header('Main Dashboard')


# Defining ticker variables
eurusd = 'EURUSD=X'
gbpusd = 'GBPUSD=X'
eurcad = 'EURCAD=X'
usdhkd = 'HKD=X'

# Access data from Yahoo Finance
eurusd_Data = yf.Ticker(eurusd)
gbpusc_Data = yf.Ticker(gbpusd)
eurcad_Data = yf.Ticker(eurcad)
usdhkd_Data = yf.Ticker(usdhkd)

# Fetch history data from Yahoo Finance
eurusdHis = eurusd_Data.history(period='max')
gbpusdHis = gbpusc_Data.history(period='max')
eurcadHis = eurcad_Data.history(period='max')
usdhkdHis = usdhkd_Data.history(period='max')

# Fetch crypto data for the dataframe
EUR_USD = yf.download(eurusd, start='2022-01-03', end='2022-01-07')
GBP_USD = yf.download(gbpusd, start='2022-01-03', end='2022-01-07')
EUR_CAD = yf.download(eurusd, start='2022-01-03', end='2022-01-07')
USD_HKD = yf.download(usdhkd, start='2022-01-03', end='2022-01-07')

# EUR/USD
st.write('EUR/USD ($)')
imageEURUSD = Image.open(urlopen('https://indexaco.com/articles_files/5713/eurusd-6.jpg'))

# Display image
st.image(imageEURUSD)

# Display dataframe
st.table(EUR_USD)

#Display a Chart
st.bar_chart(eurusdHis.Close)

# GBP/USD
st.write('GBP/USD ($)')
imageGBP_USD = Image.open(urlopen('https://indianmarketview.com/wp-content/uploads/GBPUSD-Currency-Pair.jpg'))

# Display image
st.image(imageGBP_USD)

# Display dataframe
st.table(GBP_USD)

#Display a Chart
st.bar_chart(gbpusdHis.Close)

# EUR/CAD
st.write('EUR/CAD ($)')
imageEUR_CAD = Image.open(urlopen('https://www.tradingpedia.com/wp-content/uploads/2014/11/euro-canadian-dollar-300x168.jpg'))

# Display image
st.image(imageEUR_CAD)

# Display dataframe
st.table(EUR_CAD)

#Display a Chart
st.bar_chart(eurcadHis.Close)

# USD/HKD
st.write('USD/HKD ($)')
imageUSD_HKD = Image.open(urlopen('https://www.forex.academy/wp-content/uploads/2020/01/Webp.net-resizeimage-18-640x435.jpg'))

# Display image
st.image(imageUSD_HKD)

# Display dataframe
st.table(USD_HKD)

#Display a Chart
st.bar_chart(usdhkdHis.Close)