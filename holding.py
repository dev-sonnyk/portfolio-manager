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

    def get_recent_quote(self) :
        self.recent_quote = get_json('%s:%s'%(self.market, self.code))[0]['l']

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
        diff = (price - self.target_price) * shares
        if diff < 0 :
            result = 'Loss'
            diff = diff * (-1)
        else :
            result = 'Profit'
        print('$%.2f returned -> %s of $%.2f' % (price * shares, result, diff))

        # Update info
        self.shares -= shares
        if (self.shares == 0) :
            self.price = 0
            self.book_cost = 0
        else :
            self.book_cost -= price * shares
        self.set_target_price()
