import requests


endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={"content": 'Hello World'})

# print(get_response.headers)

# print(get_response.text)
print(get_response.json())

# print(get_response.status_code)