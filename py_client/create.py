import requests
from pprint import pprint

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'This field is done'
}

get_response = requests.post(endpoint, json=data)

pprint(get_response.json())