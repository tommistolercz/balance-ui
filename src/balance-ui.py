import requests
from flask import Flask, render_template


# env
APP_HOST = '127.0.0.1'
APP_PORT = 5000

# init app
app = Flask(__name__)


# Homepage
@app.route('/')
def index():
    """
    Homepage
    """
    # get the latest data from balance history
    r = requests.get('http://127.0.0.1:5001/balance-history/latest')
    latest = r.json()

    # reformat data for template
    # thousands separated by spaces
    latest['total_amount'] = '{:,}'.format(latest['total_amount']).replace(',', ' ')
    # YYYYMMDD -> DD.MM.YYYY
    latest['date'] = '{}.{}.{}'.format(latest['date'][6:8], latest['date'][4:6], latest['date'][0:4])

    return render_template('index.html', latest=latest)


# main
if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)
