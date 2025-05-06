from django.shortcuts import render
import requests

def index(request):
    stock_name = 'IBM'
    URL = 'https://www.alphavantage.co/query'
    PARAMS = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': stock_name,
        'interval': '5min',
        'apikey': 'demo'
    }

    req = requests.get(url=URL, params=PARAMS)
    data = req.json()

    stock_data = data.get('Time Series (5min)', {})
    dataset = []

    for timestamp, values in stock_data.items():
        # Parse timestamp string into ISO-like date format
        sets = {
            'x': timestamp,  # We'll parse it in JS
            'y': [
                float(values["1. open"]),
                float(values["2. high"]),
                float(values["3. low"]),
                float(values["4. close"])
            ]
        }
        dataset.append(sets)

    # Reverse to have the oldest first
    dataset.reverse()

    return render(request, 'investo/index.html', {
        'name': stock_name,
        'stockname': stock_name,
        'data': dataset
    })
