import requests

BASE = 'http://download.finance.yahoo.com/d/quotes.csv?e=.csv'
FUNC = 'l1' #Last trade price

def request(tickers) :
    try :
        url = BASE + '&s=' + tickers + '&f=' + FUNC
        response = requests.get(url)

        return response.text.split('\n')
    except requests.ConnectionError :
        print('No Connection')
        return -1
