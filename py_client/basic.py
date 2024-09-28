import requests


endpoint = "http://127.0.0.1:8000/"


get_response = requests.get(endpoint, json={'query': 'Hello World'})


print(get_response.text)

print(get_response.status_code)