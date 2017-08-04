import csv
from holding import *
from portfolio import *

EQUITY = {} #list of equity code

def setup(filename):
    with open(filename, newline='') as csvfile :
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader : process(row)
    return Portfolio(EQUITY)

# Save holding info in data structure
def process(row):
    if (row[0] not in EQUITY) :
        EQUITY[row[0]] = Holding(row[0], row[1], float(row[2]), float(row[3]))
    else :
        EQUITY[row[0]].buy(float(row[2]), float(row[3]))

def display(l) :
    for item in l :
        print('%s in %s : %d of $%.2f | break-even sell at $%.2f' %
        (l[item].code, l[item].market, l[item].shares,
         l[item].price, l[item].target_price))

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
            display(EQUITY)
        elif (cont == 'rest'):
            portfolio = setup('portfolio.csv')
            continue
        else :
            inputs = func.split(' ')
            if (inputs[0] == 'cost') :
                holding = EQUITY[inputs[1].upper()]
                print('book cost of %s:%s is  $%.2f' %
                (holding.code, holding.market, holding.book_cost))
            elif (inputs[0] == 'sell') :
                holding = EQUITY[inputs[1].upper()]
                holding.sell(float(inputs[2]), float(inputs[3]))
        print('-------------------------------------------------------')
        cont = input('continue? [press enter]\n\t Type quit to exit\n')
        if (cont == 'quit') :
            exit()
        else :
            continue

main()
