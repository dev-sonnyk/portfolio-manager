#from googlefinance import *
from alpha import *
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
        # Google Finance API
        js = request(self.symbols)
        for j in js :
            if (j['t'] not in self.holdings) :
                print('Wrong code (%s) bro.'%(j['t']))
            else :
                self.holdings[j['t']].recent_quote = float(j['l'])
        '''
        # Alphavantage API
        for s in self.holdings :
            stock = self.holdings[s]
            self.holdings[s].recent_quote = \
                float(request(stock.code, stock.market))
        os.system('clear')

    def update(self) :
        self.set_recent_quote()
        self.set_total_cost()
        self.set_worth()

    def reset(self) : self.holdings = {}
