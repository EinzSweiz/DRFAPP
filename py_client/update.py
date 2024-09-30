import requests

endpoint = 'http://localhost:8000/api/products/14/update/'

data = {
    'title': 'Hello Darkness My old friend',
    'price': 150
}

response_data = requests.put(endpoint, data=data)

print(response_data.json())