print("Hello stocks")

# Create a dictionary
stockdict = {
             "K": "Kellogg Company", 
             "P": "Pandora Media, Inc",
             "HBI": "Hanesbrands Inc",
             "HCA": "HCA Healthcare, Inc"
            }

print(stockdict)

for ticker, name in stockdict.items():
    print("Ticker symbol is %s for %s." %(ticker, name))

# Create list of stocks
purchases = [
             ('K', 100, '21-july-2017', 96),
             ('P', 231, '09-june-2017', 102),
             ('HBI', 87, '08-march-2016', 55),
             ('HCA', 63, '12-feb-2018', 48)
            ]

for purchase in purchases:
    ticker = purchase[0]
    stock_value = purchase[1]
    date = purchase[2]
    amount_purchased = purchase[3]
    purchase_price = stock_value * amount_purchased
    company_name = stockdict[ticker]

    print(purchase_price)

for ticker, name in stockdict.items():
    total = 0