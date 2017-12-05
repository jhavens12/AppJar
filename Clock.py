from appJar import gui
import requests
from exchanges.coindesk import CoinDesk
from time import sleep
from datetime import datetime

time = datetime.now()

def update_label():
    time = datetime.now()
    app.clearLabel('L1')
    app.setLabel('L1',time)

app = gui('Test1' '480x320')
app.setGeometry('fullscreen')

#while True:
#price = CoinDesk.get_current_price(currency='USD')
#app.setBg('black')
app.setPollTime(1000)
app.setFont(72)
app.addLabel('L1', time, 1,1,3)
app.setLabelFg('L1', 'blue')


app.registerEvent(update_label)



app.go()
