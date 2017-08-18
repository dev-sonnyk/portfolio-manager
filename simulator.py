import csv
import pandas as pd
from holding import *
from portfolio import *

HELP = 'Choose your operation:' + \
'\n\tcost - see book cost of stock | format: cost [code]' + \
'\n\tsell - see profit | format: sell [code] [price] [share]' + \
'\n\tbuy - buy equity | format: buy [code] [price] [share]' + \
'\n\tview - over view of portfolio | format: view' + \
'\n\trest - restart the program | format: rest' + \
'\n\tquit - exit | format: exit\n' + \
'-------------------------------------------------------'

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
    p.set_total_cost()
    p.set_worth()

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
                                    d[key].price)) / d[key].price)) \
                                    if d[key].price != 0 \
                                    else pdict['Change'].append('0.00%')
        return pdict

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

def equity_validation(p, code, share) :
    if (code not in p.holdings) :
        return 0
    else :
        # Cannot sell more than what you own
        if (share > p.holdings[code].shares) : return 0
    return 1

'''
    List of available functions in simulator
'''

def out(p, inputs) : exit()

def help_message(p, inputs) : print(HELP)

def view(p, inputs) : display(p)

def restart(p, inputs) :
    p.reset()
    p = setup('portfolio.csv')
    return p

def cost(p, inputs) :
    code = inputs[1].upper()
    if (code not in p.holdings) :
        print('Code does not exist.')
    else :
        holding = p.holdings[code]
        print('Book Cost of %s:%s is  $%.2f' %
        (holding.market, holding.code, holding.book_cost))

def buy_action(p, inputs) :
    code = inputs[1].upper()
    if (len(inputs) == 4 and inputs[3] != '') :
        '''
        # New equity Handle
        if (code not in portfolio.holdings) :
            p.holdings[code] = \
                Holding(code,'?',float(inputs[2]), int(inputs[3]))
        '''
        holding = p.holdings[code]
        holding.buy(float(inputs[2]), int(inputs[3]))
        p.update()
    else :
        print ('Invalid format. >> buy [code] [price] [share]')

def sell_action(p, inputs) :
    try :
        code = inputs[1].upper()
        sell_amount = int(p.holdings[code].shares) \
            if (len(inputs) == 3 and inputs[3] != '') else inputs[3]
        sell_price = p.holdings[code].recent_quote \
            if (len(inputs) == 2 and inputs[2] != '')  else inputs[2]
        holding = p.holdings[code]
        holding.sell(float(sell_price), int(sell_amount))
        p.update()
    except IndexError or ValueError :
        print('Ivalid format - Try again')

# Available functions in dictionary to lookup 
methods = {'quit' : out, 'help' : help_message, 'view' : view, 'rest' : restart,
            'cost' : cost, 'buy' : buy_action, 'sell' : sell_action}

# Main method
if __name__ == '__main__' :
    portfolio = setup('portfolio.csv')
    print('Type help for available operations')
    while(1):
        print('-------------------------------------------------------')
        try :
            func = input('>> ')
            inputs = func.lower().split(' ')
            if inputs[0] == 'rest' :
                portfolio = methods[inputs[0].lower()](portfolio, inputs)
            else :
                methods[inputs[0].lower()](portfolio, inputs)
        except KeyError or IndexError:
            print('Invalid input')
        print('-------------------------------------------------------')
