This is a console application for my investment portfolio management.  (Requires Python 3.x, Pandas, urllib, requests, numPy)

If a program doesn't run properly, make sure you "pip3 install" any libraries missing. 

Sep.6.2017 >> Google Finacne API stopped working.  I am trying to replace real-time quote with https://www.alphavantage.co/

October.23.2017 >> To improve the speed performance, I implented Yahoo Finance API where I can request multiple stocks' information at once.  Now the speed performance is same as Google Finance API.

## How to use it

Go to this application directory and type 
```
python3 simulator.py
```

## View

> Format : view

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/view.png)

## Setup
![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/setup.png)

## Help

> Format : help

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/help.png)

## Buy

> Format : buy *[code]* *[price]* *[share_amount]*

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/buy.png)

## Sell

> Format : sell *[code]* *[price (optional)]* *[share_amount (optional)]*

Without share amount (it will sell all shares) / Without price will sell at last bid price

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/sell-noparam.png)


With share amount

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/sell.png)

## Cost

> Format : cost *[code]*

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/cost.png)

## Restart

> Format : rest

![alt text](https://github.com/dev-sonnyk/portfolio-manager/raw/master/images/restart.png)

## Thank you

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[GoogleFinance API example](https://github.com/hongtaocai/googlefinance/blob/master/googlefinance/__init__.py)
