import datetime
import time 
from plyer import notification 
import yfinance as yf 

msft = yf.Ticker("MSFT")
data = msft.info

while True:
    notification.notify(
        title= "MSFT data".format(datetime.date.today()),
        message= "Current Price = {cp} \nDayLow = {dl} \nDayHeigh = {dh}".format(
            cp = data["currentPrice"],
            dl = data["regularMarketDayLow"],
            dh = data["regularMarketDayHigh"],
        ),
        app_icon = "notification.ico",
        timeout = 10
    )
    time.sleep(20)