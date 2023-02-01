import requests
import pytest

url = 'http://127.0.0.1:5000/delivery-fee'

def test_api_status_codes():
    # Status 200
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    assert response.status_code == 200

    # Status 400 if one of the parameters is missing
    response = requests.post(url, json={'delivery_distance': 2235, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    assert response.status_code == 400


def test_calculate_delivery_fee():
    # Example from the specification
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 710

    # If the delivery distance is shorter than 1 km, base fee is 2€ for the first 1km
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 900, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 410

    # If the delivery distance is longer than 1 km, extra fee is 1€ for each 500m. Extra fee is 3€ (1000m - 2€, 499m - 1€)
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 1499, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 510

    # extra fee is 3€ (1000m - 2€, 500m - 1€)
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 1500, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 510

    # extra fee is 4€ (1000m - 2€, 500m - 1€, 1m - 1€)
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 1501, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 610

    # If the cart value more than 100€ the delivery fee is 0€
    response = requests.post(url, json={'cart_value': 10000, 'delivery_distance': 2235, 'number_of_items': 4, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 0

    # If the number of items more than 4, extra fee is 0.5€ for each item
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 10, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 1010

    # If the number of items more than 12, extra 'bulk' is 1.2€
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 13, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 1280

    # The delivery fee can not be more than 15€. Calculated delivery fee 2020 = 20.2€ (base_fee 200€ + small_cart_value_surcharge 500€ + add_distance_surcharge 400€ + add_items_surcharge 800€ + extra_surcharge 120€)
    response = requests.post(url, json={'cart_value': 500, 'delivery_distance': 3000, 'number_of_items': 20, 'time': '2021-10-12T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 1500

    # Friday rush(3 - 7 PM UTC) the delivery fee will be multiplied by 1.2x.  
    # The delivery day is Friday, but not between 3 and 7 pm. 
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 4, 'time': '2021-10-15T13:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 710

    # The delivery day is Friday and between 3 and 7 pm (750 * 1.2). 
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 4, 'time': '2021-10-15T16:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 852

    # The delivery day is Friday and between 3 and 7 pm (1280 * 1.2 = 1536), but it can not be more than 15€ 
    response = requests.post(url, json={'cart_value': 790, 'delivery_distance': 2235, 'number_of_items': 13, 'time': '2021-10-15T16:00:00Z'})
    result = response.json()
    assert result['delivery_fee'] == 1500