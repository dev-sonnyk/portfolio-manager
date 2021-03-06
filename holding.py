FEE = 9.95

class Holding :
    def __init__(self, code, market, price, shares) :
        self.code = code
        self.market = market
        self.price = price
        self.shares = shares
        self.book_cost = self.price * self.shares + FEE
        self.target_price = (self.book_cost + FEE) / self.shares
        self.recent_quote = 0
        print('Bought %d of %s -> $%.2f'%(shares, self.code, price * shares))

    def set_target_price(self) :
        self.target_price = (self.book_cost + FEE) / self.shares \
            if self.shares != 0 else 0

    def buy(self, price, shares) :
        new_cost = price * shares
        self.price = (self.price * self.shares + new_cost) / (self.shares + shares)
        self.shares += shares
        self.book_cost += (new_cost + FEE)
        self.target_price = (self.book_cost + FEE) / self.shares
        print('Bought %d of %s -> $%.2f'%(shares, self.code, price * shares))

    def sell(self, price, shares) :
        diff = (abs(price) - self.target_price) * shares
        sign = '-' if diff < 0 else ''
        print('Sold %d of %s $%.2f returned (%s$%.2f)'%
            (shares, self.code, abs(price) * shares - FEE, sign, abs(diff)))

        # Update info
        self.shares -= shares
        if (self.shares == 0) :
            self.price = 0
            self.book_cost = 0
        else :
            self.book_cost = self.price * self.shares
        self.set_target_price()
        return diff
