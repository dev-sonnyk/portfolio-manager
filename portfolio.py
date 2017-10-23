#from alpha import *
from yahoo import *
import json
import os

class Portfolio:
    def __init__(self, holdings, symbols) :
        self.holdings = holdings
        self.symbols = symbols
        self.total_cost = 0
        self.worth = 0
        self.fund = 0
        self.perform = 0

    def set_total_cost(self) :
        self.total_cost = 0
        for stock in self.holdings :
            self.total_cost += float(self.holdings[stock].book_cost)

    def set_worth(self) :
        self.worth = 0
        for stock in self.holdings :
            self.worth += float(self.holdings[stock].recent_quote *
                            self.holdings[stock].shares)

    def set_recent_quote(self) :
        '''
        # Alphavantage API
        for s in self.holdings :
            stock = self.holdings[s]
            last_close = float(request(stock.code, stock.market))
            while last_close == -1 :
                last_close = float(request(stock.code, stock.market))
            self.holdings[s].recent_quote = last_close
        '''
        # Yahoo Finance API
        tickers = ''
        for symbol in self.symbols :
            ticker = symbol.split(':')[1]
            market = symbol.split(':')[0]
            tickers += ticker
            if market == 'TSE' : tickers += '.TO'
            tickers += ','
        quotes = request(tickers[:-1])
        trial = 0
        while quotes == -1 and trial != 5:
            quotes = request(tickers[:-1])
            trial += 1
        i = 0
        for s in self.holdings :
            self.holdings[s].recent_quote = float(quotes[i])
            i += 1

        os.system('clear')

    def update(self) :
        try :
            self.set_recent_quote()
            self.set_total_cost()
            self.set_worth()
            return 1
        except KeyError :
            return 0

    def remove(self, code, market) :
        del self.holdings[code]
        self.symbols.remove('%s:%s'%(market,code))

    def reset(self) : self.holdings = {}
