from appJar import gui
import requests
from exchanges.coindesk import CoinDesk
from time import sleep
from datetime import datetime

time = datetime.now()
timestamp = str(time.time().strftime('%I:%M %p'))


price = '${:,.2f}'.format(CoinDesk.get_current_price(currency='USD'))

def update_label():
    time = datetime.now()
    timestamp = str(time.time().strftime('%I:%M %p'))
    price = '${:,.2f}'.format(CoinDesk.get_current_price(currency='USD'))
    app.clearLabel('L1')
    app.setLabel('L1',price)
    app.clearLabel('L2')
    app.setLabel('L2',timestamp)

app = gui('Test1' '480x320')
app.setGeometry('fullscreen')

app.setPollTime(30000)
app.setFont(72)
app.addLabel('L1', price, 1,1,3)
app.addLabel('L2', timestamp, 2,1,3)
app.setLabelFg('L1', 'blue')
app.setLabelFg('L2', 'red')
app.getLabelWidget("L2").config(font="Courier 20")
app.registerEvent(update_label)

app.go()
