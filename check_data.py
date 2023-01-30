from flask import abort

def check_data(data):
    arguments = ['cart_value', 'delivery_distance', 'number_of_items', 'time']

    for i in range(3):
        if arguments[i] not in data:
            err = f'The argument {arguments[i]} is missing'
            abort(400, err)
