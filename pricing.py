
from alpha_vantage.timeseries import TimeSeries
# Your key here
#key = 'yourkeyhere'
#ts = TimeSeries(key)
#aapl, meta = ts.get_daily(symbol='AAPL')
#print(aapl['2019-09-12'])



# load environment variables
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
alphaAdvantageAPI = os.getenv('AlphaAdvantageAPI')

from alpha_vantage.timeseries import TimeSeries
key = alphaAdvantageAPI
ts = TimeSeries(key)
def quoteParse(ts):
    aapl, meta = ts.get_daily(symbol='GLD')
    dateObject = aapl['2020-01-15']
    print(dateObject['1. open'])
       
quoteParse(ts)