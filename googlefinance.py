import json

try :
    from urllib.request import Request, urlopen
except ImportError :
    from urllib2 import Request, urlopen

BASE = 'http://finance.google.com/finance/info?client=ig&q='

def build_url(symbols) :
    symbol_list = ','.join([symbol for symbol in symbols])
    return BASE + symbol_list

def request(symbols) :
    if (type(symbols) == str) : symbols = [symbols]
    url = build_url(symbols)
    req = Request(url)
    response = urlopen(req)
    content = response.read().decode('ascii', 'ignore').strip()
    return content[3:]

def get_last_bid(symbols) :
    j = json.loads(request(symbols))[0]
    return float(j['l'])
