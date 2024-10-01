import requests
from pprint import pprint

endpoint = 'http://localhost:8000/api/products/'

headers = {
    'Authorization': 'Bearer f882dddce1c39db4e22e81746e78c3c9ace9ab9c'
}


data = {
    'title': 'This field is done'
}

get_response = requests.post(endpoint, json=data, headers=headers)

pprint(get_response.json())