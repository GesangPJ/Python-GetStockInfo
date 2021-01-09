#Get packages
import yfinance as yf
import time
ticket = input("Please enter stock symbol : ")
periody = input("Please enter period you want (1d/5d/1mo/3mo/6mo/1y/2y/...max) : ")
intv = input("Please enter interval you want (60m/1d/1wk/1mo/3mo) :")

stockd = yf.download(tickers=ticket,period=periody,interval=intv, threads=True)

stockd.to_csv( ticket +"-"+periody+"-"+"data.csv")