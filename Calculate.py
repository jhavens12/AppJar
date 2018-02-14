
purchase = []
btc = []
fee = []

purchase.append(122.44) #initial purchase 12/5/17 at $11,774
btc.append(.01) #initital purchase 12/5/17 at $11,774
fee.append(-.00035361) #transfer to wallet 12/7/17

purchase.append(120)
btc.append(.00716809)

price = input("Current Rate? ")
worth = float(price) * sum(btc+fee)
worth_USD = '${:,.2f}'.format(float(price) * sum(btc+fee))
margin = worth - sum(purchase)
margin_USD = '${:,.2f}'.format(margin)

print()
print("Total BTC: "+str(sum(btc+fee)))
print("Margin: "+margin_USD)
print("Worth: "+worth_USD)
