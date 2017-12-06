import requests
from exchanges.coindesk import CoinDesk
from time import sleep
from datetime import datetime
import socket
import ui
import console

import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
import pylab
from io import BytesIO

invested = 122.44
owned = .01

n = 1

x_list = []
y_list = []

# time = datetime.now()
# timestamp = str(time.time().strftime('%I:%M %p'))
#
# price = CoinDesk.get_current_price(currency='USD')
# price_USD = '${:,.2f}'.format(price)
# worth = float(price) * owned
# worth_USD = '${:,.2f}'.format(float(price) * owned)
# margin = worth - invested
# margin_USD = '${:,.2f}'.format(margin)
#
# x_list.append(time)
# y_list.append(price)

v = ui.load_view()
v.background_color = "black"

label1= v['label1']
label2= v['label2']
label3= v['label3']
label4= v['label4']

def graph(x_list,y_list):
    plt.clf()

    plt.style.use('dark_background')
    plt.axis('off')
    plt.rcParams['lines.linewidth'] = 5
    plt.plot(x_list,y_list, color='red')
    #plt.ylim(ymin=0)

    b = BytesIO()
    plt.savefig(b, bbox_inches='tight', transparent='True')

    v['imageview1'].image = ui.Image.from_data(b.getvalue())


def update_labels():

    time = datetime.now()
    timestamp = str(time.time().strftime('%I:%M %p'))


    price = CoinDesk.get_current_price(currency='USD')
    price_USD = '${:,.2f}'.format(price)
    worth = float(price) * owned
    worth_USD = '${:,.2f}'.format(float(price) * owned)
    margin = worth - invested
    margin_USD = '${:,.2f}'.format(margin)

    if margin > 0:
        label2.text_color = 'green'
    else:
        label2.text_color = 'red'

    x_list.append(time)
    y_list.append(price)

    label1.text = price_USD
    label2.text = margin_USD
    label3.text = timestamp

    graph(x_list,y_list)

graph(x_list,y_list)
update_labels()

v.present(style='sheet', hide_title_bar=True)

while True:
  update_labels()
  n = n+1
  label4.text = str(n)
  sleep(5)
