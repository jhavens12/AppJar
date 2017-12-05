from appJar import gui
import requests
from exchanges.coindesk import CoinDesk
from time import sleep
from datetime import datetime
import socket
import os
import sys

current_ip = socket.gethostbyname(socket.gethostname())

if current_ip == "127.0.1.1":

    gam_input = "ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'"
    result_1 = os.popen(gam_input).read()
    current_ip = result_1


invested = 122.44
owned = .01

time = datetime.now()
timestamp = str(time.time().strftime('%I:%M %p'))

price = CoinDesk.get_current_price(currency='USD')
price_USD = '${:,.2f}'.format(price)
worth = float(price) * owned
worth_USD = '${:,.2f}'.format(float(price) * owned)
margin = worth - invested
margin_USD = '${:,.2f}'.format(margin)

def update_label():
    time = datetime.now()
    timestamp = str(time.time().strftime('%I:%M %p'))
    price = CoinDesk.get_current_price(currency='USD')
    price_USD = '${:,.2f}'.format(price)
    worth = float(price) * owned
    worth_USD = '${:,.2f}'.format(float(price) * owned)
    margin = worth - invested
    margin_USD = '${:,.2f}'.format(margin)

    app.clearLabel('L1')
    app.setLabel('L1',price_USD)

    app.clearLabel('L2')
    app.setLabel('L2',margin_USD)
    if margin > 0:
        app.setLabelFg('L2', 'dark green')
    else:
        app.setLabelFg('L2', 'red')

    app.clearLabel('L3')
    app.setLabel('L3',timestamp)

app = gui('Test1' '480x320')
app.setGeometry('fullscreen')
app.setBg('black')

app.setPollTime(30000)
app.setFont(64)
app.addLabel('L1', price_USD, 1,1,3)
app.addLabel('L2', margin_USD, 2,1,3)
app.addLabel('L3', timestamp, 3,1,1)
app.addLabel('L4', current_ip, 3,3,1)
app.setLabelFg('L1', 'blue')

if worth > 0:
    app.setLabelFg('L2', 'dark green')
else:
    app.setLabelFg('L2', 'red')

app.setLabelFg('L3', 'white')
app.setLabelFg('L4', 'white')
app.getLabelWidget("L2").config(font="Verdana 44")
app.getLabelWidget("L3").config(font="Verdana 10")
app.getLabelWidget("L4").config(font="Verdana 10")
app.registerEvent(update_label)

app.go()
