# Wolt Pre-assignment Backend

### Technologies:
* Python3
* Flask

### Installation
Run in the project directory: 

`source py_create.sh`    

`.\py_create.bat`        if you use Windows 

### To start server run in the project directory:
`(wolt-env)  python3 main.py`

`(wolt-env)  python main.py`.  if you use Windows 

The server is running on port http://127.0.0.1:5000

### To run tests: 
In a new terminal activate virtual environment:

`source ./wolt-env/bin/activate`

`wolt-evn\scripts\activate` if you use Windows 

and run tests:

`(wolt-env)  pytest tests.py`

### Testing API requests with Postman.

* URI: http://127.0.0.1:5000/delivery-fee 
* method: POST
* header Content-Type: application/json
* body JSON:
```
{
    "cart_value": 790,
    "delivery_distance": 2235,
    "amount_of_items": 4,
    "time": "2021-10-12T13:00:00Z"
}
```
