import json

try :
    from urllib.request import Request, urlopen
    import urllib.error
except ImportError :
    print('Download Python3 and urllib')
    exit()

BASE = 'http://finance.google.com/finance/info?client=ig&q='

def build_url(symbols) :
    symbol_list = ','.join([symbol for symbol in symbols])
    return BASE + symbol_list

def request(symbols) :
    content = ''
    i = 0
    while (content == '' and i < 10) :
        try :
            if (type(symbols) == str) : symbols = [symbols]
            url = build_url(symbols)
            req = Request(url)
            response = urlopen(req)
            content = response.read().decode('ascii', 'ignore').strip()
        except urllib.error.URLError :
            print('Check Internet Connection or URL')
            content = ''
            i += 1
    return json.loads(content[3:]) if content != '' else quit()
