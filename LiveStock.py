#Get packages
import yfinance as yf

stocksym = input("Please enter stock symbol : ")
periode = input("Please enter period you want (1d/5d/1mo/3mo/6mo/1y/2y/...max) : ")


sts = yf.Ticker(stocksym)

sts.history(period=periode)