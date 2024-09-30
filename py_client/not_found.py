import requests

endpoint = 'http://localhost:8000/api/products/3166332673217637321'

response_data = requests.get(endpoint)
print(response_data.json())