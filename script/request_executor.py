from time import sleep

import requests

endpoint1 = "http://127.0.0.1:8000/sync/check-object-count"  # No leak
endpoint2 = "http://127.0.0.1:8000/intended_mem_leak"  # leak
endpoint3 = "http://127.0.0.1:8000/sync/pydantic"  # No leak
endpoint4 = "http://127.0.0.1:8000/async/pydantic"  # No leak
endpoint5 = "http://127.0.0.1:8000/sync/di-container"  # No leak
endpoint6 = "http://127.0.0.1:8000/sync/intended_exception"  # No leak
endpoint7 = "http://127.0.0.1:8000/async/intended_exception"  # No leak
endpoint8 = "http://127.0.0.1:8000/sync/hierarchy-pydantic"  # No leak
endpoint9 = "http://127.0.0.1:8000/async/hierarchy-pydantic"  # No leak

# GET request
# while True:
#     response = requests.get(endpoint8)
#     print(response.json())


# POST request
# while True:
#     response = requests.post(endpoint4, json={"name": "test", "description": "test"})
#     print(response.json())


# iterate over all endpoints
while True:
    response = requests.get(endpoint1)
    print(response.json())
    response = requests.get(endpoint2)
    print(response.json())
    response = requests.post(endpoint3, json={"name": "test", "description": "test"})
    print(response.json())
    response = requests.post(endpoint4, json={"name": "test", "description": "test"})
    print(response.json())
    response = requests.get(endpoint5)
    print(response.json())
    response = requests.get(endpoint6)
    print(response.json())
    response = requests.get(endpoint7)
    print(response.json())
    response = requests.get(endpoint8)
    print(response.json())
    response = requests.get(endpoint9)
    print(response.json())
