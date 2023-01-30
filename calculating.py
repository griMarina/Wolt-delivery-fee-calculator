import math
from datetime import datetime


def calculate_delivery_fee(cart_value, delivery_distance, number_of_items, delivery_data):

    base_fee = 200

    small_cart_value_surcharge = max(0, 1000 - cart_value)

    add_distance = delivery_distance - 1000
    add_distance_surcharge = max(0, math.ceil(add_distance / 500) * 100)

    add_items_surcharge = max(0, ((number_of_items - 4) * 50))
    extra_surcharge = 120 if number_of_items > 12 else 0

    delivery_fee = base_fee + small_cart_value_surcharge + \
        add_distance_surcharge + add_items_surcharge + extra_surcharge

    delivery_data = datetime.strptime(delivery_data, "%Y-%m-%dT%H:%M:%SZ")

    if delivery_data.strftime("%A") == "Friday" and int(delivery_data.strftime("%H")) >= 15 and int(delivery_data.strftime("%H")) < 19:
        delivery_fee *= 1.2

    delivery_fee = 0 if cart_value >= 10000 else delivery_fee

    return min(delivery_fee, 1500)
