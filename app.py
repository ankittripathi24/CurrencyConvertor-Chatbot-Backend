from flask import Flask, request, jsonify
import requests


app =  Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    print(data)
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    source_currency_amount = data['queryResult']['parameters']['unit-currency']['amount']
    desti_currency = data['queryResult']['parameters']['currency-name'][0]
    print(source_currency)
    print(desti_currency)
    print(source_currency_amount)
    val = converter(source_currency, source_currency_amount, desti_currency)
    print("CONVERTED VALUE= ", val)

    response = {
        'fulfillmentText': "{} {} is {} {}".format(source_currency_amount, source_currency, val, desti_currency)
    }

    return jsonify(response)

def converter(source_currency, source_currency_amount, desti_currency ):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_QyLZWenyqGocRMIP9Lxdxvz6t0SEoUOnnEzdxVgP"
    response = requests.get(url)
    response = response.json()
    print(response['data'][source_currency])
    print(response['data'][desti_currency])


    x = int(source_currency_amount) * int((response['data'][desti_currency] / response['data'][source_currency]))
    return x

if __name__ == "__main__":
    app.run(debug=True)