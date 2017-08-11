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
    portfolio = Portfolio(equity_dict)
    portfolio.set_recent_quote(request_symbols)
    portfolio.set_worth()
    portfolio.set_total_cost()
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
        pdict['Percentage'].append('%.2f%%'%((100.0 * d[key].book_cost) / p.total_cost))
        pdict['Change'].append('%.2f%%'%((100 * (d[key].recent_quote -
                                d[key].price)) / d[key].price))
    return pdict

if __name__ == '__main__' :
    first = True
    portfolio = setup('portfolio.csv')
    while(1):
        print('')
        print('-------------------------------------------------------')
        if (first) :
            func = input('Choose your operation:' +
            '\n\tcost - see book cost of stock (e.g cost googl)' +
            '\n\tsell - see profit | format: sell [code] [price] [share]' +
            '\n\tview - over view of portfolio (no paramater)' +
            '\n\trest - restart the program' +
            '\n\tquit - exit\n')
            print('-------------------------------------------------------')
        else :
            func = input('Type your function here: ')
        if (func == 'quit') :
            exit()
        elif (func == 'view'):
            display(portfolio)
        elif (func == 'rest'):
            portfolio.reset()
            portfolio = setup('portfolio.csv')
        else :
            inputs = func.split(' ')
            if (inputs[0] == 'cost') :
                if (len(inputs) == 1) :
                    print('%.2f'%(portfolio.total_cost))
                else :
                    holding = portfolio.holdings[inputs[1].upper()]
                    print('book cost of %s:%s is  $%.2f' %
                    (holding.market, holding.code, holding.book_cost))
            elif (inputs[0] == 'buy') :
                holding = portfolio.holdings[inputs[1].upper()]
                holding.buy(float(inputs[2]), float(inputs[3]))
            elif (inputs[0] == 'sell') :
                if (len(inputs) < 4) :
                    sell_amount = int(portfolio.holdings[inputs[1].upper()].shares)
                else :
                    sell_amount = inputs[3]
                holding = portfolio.holdings[inputs[1].upper()]
                holding.sell(float(inputs[2]), float(sell_amount))
        print('-------------------------------------------------------')
        first = False
        '''
        cont = input('continue? [press enter]\n\t Type quit to exit\n')
        if (cont == 'quit') :
            exit()
        else :
            continue
        '''
