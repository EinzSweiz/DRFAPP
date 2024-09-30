import requests 
from pprint import pprint


product_id = input('Please enter your product_id: ')


try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'This is not valid product id {product_id}.')



endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"


response_data = requests.delete(endpoint)

if '2' in str(response_data.status_code):
    print('Deleted!')
else:
    print('Error happened: not product with this id')
