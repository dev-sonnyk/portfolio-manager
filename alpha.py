import json
from urllib.request import urlopen
import urllib.error
from datetime import datetime, date

BASE = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY' \
     '&interval=1min&apikey=MMQ0UDNZAOQI7XUZ&outputsize=compact&symbol='

def request(symbol, market) :
    url = BASE + symbol.upper()
    if market == 'TSE' : url += '.TO'
    response = urlopen(url)
    content = response.read()

    ## This only works for US stocks
    # now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
    # json.loads(content)['Time Series (1min)'][now]
    print('Processing ' + symbol)
    for quote in json.loads(content)['Time Series (1min)'] :
        return json.loads(content)['Time Series (1min)'][quote]['4. close']
