from googlefinance import *
import json

class Portfolio:
    def __init__(self, holdings) :
        self.holdings = holdings
        self.total_cost = 0
        self.worth = 0

    def set_total_cost(self) :
        for stock in self.holdings :
            self.total_cost += float(self.holdings[stock].book_cost)

    def set_worth(self) :
        for stock in self.holdings :
            self.worth += float(self.holdings[stock].recent_quote)

    def set_recent_quote(self, symbols) :
        js = get_json(symbols)
        for j in js :
            if (j['t'] not in self.holdings) :
                print('Wrong code (%s) bro.'%(j['t']))
            else :
                self.holdings[j['t']].recent_quote = float(j['l'])

    def reset(self) :
        self.holdings = {}
