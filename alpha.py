import json
from urllib.request import urlopen
import urllib.error
from datetime import datetime, date

FUNC = 'TIME_SERIES_INTRADAY'
#FUNC = 'TIME_SERIES_DAILY_ADJUSTED'
BASE = 'https://www.alphavantage.co/query?function=' +  FUNC + \
     '&interval=1min&apikey=MMQ0UDNZAOQI7XUZ&outputsize=compact&symbol='

def request(symbol, market) :
    url = BASE + symbol.upper()
    if market == 'TSE' : url += '.TO'

    ## This only works for US stocks
    # now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
    # json.loads(content)['Time Series (1min)'][now]
    try :
        response = urlopen(url)
        content = response.read()
        print('Price retreived : ' + symbol)
        for quote in json.loads(content)['Time Series (1min)'] :
            return json.loads(content)['Time Series (1min)'][quote]['4. close']
    except urllib.error.URLError :
        print('Failed ' + symbol)
        return -1
