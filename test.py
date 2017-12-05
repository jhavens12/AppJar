import requests
from exchanges.coindesk import CoinDesk

print(CoinDesk.get_current_price(currency='USD'))
