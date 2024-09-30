import requests
from pprint import pprint

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.get(endpoint)


pprint(get_response.json())