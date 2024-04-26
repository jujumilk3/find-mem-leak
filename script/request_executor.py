import requests
from time import sleep


endpoint1 = "http://127.0.0.1:8000/sync/check-object-count"  # No leak
endpoint2 = "http://127.0.0.1:8000/intended_mem_leak"  # leak
endpoint3 = "http://127.0.0.1:8000/sync/pydantic"  # No leak

# GET request
# while True:
#     response = requests.get(endpoint2)
#     print(response.json())
#     sleep(1)


# POST request
while True:
    response = requests.post(endpoint3, json={"name": "test", "description": "test"})
    print(response.json())
