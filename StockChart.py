#Get packages
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

ticket = input("Please enter stock symbol : ")
periody = input("Please enter period you want (1d/5d/1mo/3mo/6mo/1y/2y/...max) : ")
intv = input("Please enter interval you want (60m/1d/1wk/1mo/3mo) :")
tipe = input("Please enter data type (High/Low/Close) : ")

data = yf.Ticker(ticket)

car = data.history(period=periody)

car[tipe].plot(figsize=(16, 9))