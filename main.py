from flask import Flask, request, jsonify
from calculating import calculate_delivery_fee
from check_data import check_data

app = Flask(__name__)

@app.route('/')
def index():
    return 'Delivery fee calculator'

@app.route('/delivery-fee', methods=['POST'])
def delivery_fee():
    data = request.get_json()
    
    check_data(data)

    delivery_fee = calculate_delivery_fee(
        data['cart_value'], data['delivery_distance'], data['number_of_items'], data['time'])

    return jsonify({"delivery_fee": delivery_fee})


if __name__ == '__main__':
    app.run()
