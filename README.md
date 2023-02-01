Wolt Pre-assignment Backend

Technologies:
* Python3
* Flask

Installation
Run in project directory:
source py_create.sh if you use mac OC
or
.\py_create.bat if you use Windows OC

To start server run in project directory:
(wolt-env)  python3 main.py

The server is running on port http://127.0.0.1:5000

To run tests 
In new terminal activate virtual environment:
source ./wolt-env/bin/activate
and run tests:
(wolt-env)  pytest tests.py

To test API requests you can use Postman.
URI: http://127.0.0.1:5000/delivery-fee 
method: POST
header Content-Type: application/json
body JSON:
{
    "cart_value": 790,
    "delivery_distance": 2235,
    "amount_of_items": 4,
    "time": "2021-10-12T13:00:00Z"
}