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
        print('Bought ' + str(shares) + ' of ' + self.code)

    def buy(self, price, shares):
        new_cost = price * shares
        self.price = (self.price * self.shares + new_cost) / (self.shares + shares)
        self.shares += shares
        self.book_cost += (new_cost + FEE)
        self.target_price = (self.book_cost + FEE) / self.shares
        print('Bought ' + str(shares) + ' of ' + self.code)

    def sell(self, price, shares):
        self.shares -= shares
        diff = (price - self.target_price) * shares
        if diff < 0 :
            result = 'Loss'
            diff = diff * (-1)
        else :
            result = 'Profit'
        print('%s of $%.2f' % (result, diff))
