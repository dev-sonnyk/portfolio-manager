import csv
import pandas as pd
from holding import *
from portfolio import *

EQUITY = {} #list of equity code

def setup(filename):
    with open(filename, newline='') as csvfile :
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader : process(row)
    portfolio = Portfolio(EQUITY)
    portfolio.set_worth()
    portfolio.set_total_cost()
    return portfolio

# Save holding info in data structure
def process(row):
    if (row[0] not in EQUITY) :
        EQUITY[row[0]] = Holding(row[0], row[1], float(row[2]), float(row[3]))
    else :
        EQUITY[row[0]].buy(float(row[2]), float(row[3]))

def display(d) :
    pdict = dict_to_pandas_friendly(d)
    column = ['Code', 'Shares', 'Price', 'Target Price', 'Last Bid']
    df = pd.DataFrame(pdict, columns=column)
    print(df)
    '''
    for item in d :
        print('%s in %s : %d of $%.2f | break-even sell at $%.2f' %
        (l[item].code, l[item].market, l[item].shares,
         l[item].price, l[item].target_price))
    '''

def dict_to_pandas_friendly(d) :
    pdict = {'Code':[], 'Shares':[], 'Price':[], 'Target Price':[],
     'Last Bid':[]}
    for key in d :
        pdict['Code'].append('%s:%s'%(d[key].market,d[key].code))
        pdict['Shares'].append(d[key].shares)
        pdict['Price'].append('%.3f'%(d[key].price))
        pdict['Target Price'].append('%.3f'%(d[key].target_price))
        pdict['Last Bid'].append(d[key].recent_quote)
    return pdict

def main() :
    portfolio = setup('portfolio.csv')
    while(1):
        print('\n')
        print('-------------------------------------------------------')
        func = input('Choose your operation:' +
        '\n\tcost - see book cost of stock (e.g cost googl)' +
        '\n\tsell - see profit | format: sell [code] [price] [share]' +
        '\n\tview - over view of portfolio (no paramater)' +
        '\n\trest - restart the program' +
        '\n\tquit - exit\n')
        print('-------------------------------------------------------')
        if (func == 'quit') :
            exit()
        elif (func == 'view'):
            display(portfolio.holdings)
        elif (func == 'rest'):
            portfolio.reset()
            portfolio = setup('portfolio.csv')
        else :
            inputs = func.split(' ')
            if (inputs[0] == 'cost') :
                holding = portfolio.holdings[inputs[1].upper()]
                print('book cost of %s:%s is  $%.2f' %
                (holding.code, holding.market, holding.book_cost))
            elif (inputs[0] == 'sell') :
                if (len(inputs) < 4) :
                    sell_amount = portfolio.holdings[inputs[1].upper()].shares
                else :
                    sell_amount = inputs[3]
                holding = portfolio.holdings[inputs[1].upper()]
                holding.sell(float(inputs[2]), float(sell_amount))
        print('-------------------------------------------------------')
        cont = input('continue? [press enter]\n\t Type quit to exit\n')
        if (cont == 'quit') :
            exit()
        else :
            continue

main()
