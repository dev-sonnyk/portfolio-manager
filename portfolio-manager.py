import csv
import pandas as pd
from holding import *
from portfolio import *

def setup(filename):
    equity_dict = {}
    request_symbols = []
    with open(filename, newline='') as csvfile :
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader : process(row, equity_dict, request_symbols)
    portfolio = Portfolio(equity_dict, request_symbols)
    portfolio.update()
    return portfolio

# Save holding info in data structure
def process(row, equity_list, symbols):
    if (row[0] not in equity_list) :
        equity_list[row[0]] = Holding(row[0], row[1], float(row[2]), int(row[3]))
        symbols.append('%s:%s'%(row[1], row[0]))
    else :
        equity_list[row[0]].buy(float(row[2]), int(row[3]))

def display(p) :
    pdict = dict_to_pandas_friendly(p)
    column = ['Percentage', 'Code', 'Shares', 'Price', 'Target Price',
    'Last Bid', 'Change']
    df = pd.DataFrame(pdict, columns=column)
    print(df)
    print('\nTotal Cost :\t$%.2f'%(p.total_cost))
    print('\nTotal Worth :\t$%.2f'%(p.worth))

    diff = p.worth - p.total_cost
    pct = 100 * diff / p.total_cost
    sign = '-' if diff < 0 else '+'
    if diff < 0 : diff = diff * -1

    print('\nTotal Change : %s$%.2f (%.2f%%)'%(sign, diff, pct))


def dict_to_pandas_friendly(p) :
    d = p.holdings
    pdict = {'Code':[], 'Shares':[], 'Price':[], 'Target Price':[],
     'Last Bid':[], 'Percentage':[], 'Change':[]}
    for key in p.holdings :
        pdict['Code'].append('%s:%s'%(d[key].market,d[key].code))
        pdict['Shares'].append('%d'%(d[key].shares))
        pdict['Price'].append('%.3f'%(d[key].price))
        pdict['Target Price'].append('%.3f'%(d[key].target_price))
        pdict['Last Bid'].append(d[key].recent_quote)
        pdict['Percentage'].append('%.2f%%'%((100.0 * d[key].book_cost) /
                                p.total_cost))
        pdict['Change'].append('%.2f%%'%((100 * (d[key].recent_quote -
                                d[key].price)) / d[key].price))
    return pdict

if __name__ == '__main__' :
    first = True
    portfolio = setup('portfolio.csv')
    while(1):
        print('-------------------------------------------------------')
        if (first) :
            func = input('Choose your operation:' +
            '\n\tcost - see book cost of stock (e.g cost googl)' +
            '\n\tsell - see profit | format: sell [code] [price] [share]' +
            '\n\tview - over view of portfolio (no paramater)' +
            '\n\trest - restart the program' +
            '\n\tquit - exit\n>> ')
            print('-------------------------------------------------------')
        else :
            func = input('>> ')
        if (func.lower() == 'quit') :
            exit()
        elif (func.lower() == 'view'):
            display(portfolio)
        elif (func.lower() == 'rest'):
            portfolio.reset()
            portfolio = setup('portfolio.csv')
        else :
            inputs = func.lower().split(' ')
            if (inputs[0] == 'cost') :
                if (len(inputs) == 1) :
                    print('%.2f'%(portfolio.total_cost))
                else :
                    holding = portfolio.holdings[inputs[1].upper()]
                    print('Book Cost of %s:%s is  $%.2f' %
                    (holding.market, holding.code, holding.book_cost))
            elif (inputs[0] == 'buy') :
                holding = portfolio.holdings[inputs[1].upper()]
                holding.buy(float(inputs[2]), float(inputs[3]))
                portfolio.update()
            elif (inputs[0] == 'sell') :
                sell_amount = int(portfolio.holdings[inputs[1].upper()].shares) \
                    if len(inputs) < 4 else inputs[3]
                holding = portfolio.holdings[inputs[1].upper()]
                holding.sell(float(inputs[2]), float(sell_amount))
                portfolio.update()
        print('-------------------------------------------------------')
        first = False
        '''
        cont = input('continue? [press enter]\n\t Type quit to exit\n')
        exit() if (cont == 'quit') else continue
        '''
