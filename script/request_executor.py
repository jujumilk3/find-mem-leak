from time import sleep

import requests

endpoint1 = "http://127.0.0.1:8000/sync/check-object-count"  # No leak
endpoint2 = "http://127.0.0.1:8000/intended_mem_leak"  # leak
endpoint3 = "http://127.0.0.1:8000/sync/pydantic"  # No leak
endpoint4 = "http://127.0.0.1:8000/async/pydantic"  # No leak
endpoint5 = "http://127.0.0.1:8000/sync/di-container"  # No leak

# GET request
while True:
    response = requests.get(endpoint5)
    print(response.json())


# POST request
# while True:
#     response = requests.post(endpoint4, json={"name": "test", "description": "test"})
#     print(response.json())
