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

    def reset(self) :
        self.holdings = {}
