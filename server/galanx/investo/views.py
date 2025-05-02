from django.shortcuts import render
import requests  # Correct module for making HTTP requests

# Create your views here.
def index(request):
    stock_name = 'IBM'
    URL = 'https://www.alphavantage.co/query'
    PARAMS = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stock_name,
        'interval': '5min',
        'apikey': 'demo'
    }

    # Make the GET request using the 'requests' library
    req = requests.get(url=URL, params=PARAMS)
    data = req.json()  # Make sure to call json()

    return render(request, 'investo/index.html', {
        'name': stock_name,
        'stockname': stock_name,
        'data': data
    })
