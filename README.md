# Wolt Pre-assignment Backend

### Technologies:
* Python3
* Flask

### Installation
Run in the project directory: `source py_create.sh` on Unix

or `.\py_create.bat` on Windows and activate virtual environment `.\wolt-env\scripts\activate` if it hasn't activated yet.

### Start server 
Run in the project directory: `python3 main.py` on Unix

or `python main.py` on Windows 

The server is running on port http://127.0.0.1:5000

### Testing: 
In a new terminal activate virtual environment: `source ./wolt-env/bin/activate`  on Unix

or `.\wolt-env\scripts\activate` on Windows 

Run tests: `pytest tests.py`

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
