import requests
import json


URL = "http://localhost:8000/api2/category/create"
data = {
    'name' : 'Aspark',
    'description' : 'hey mahesh',
    'category_id' : 'mah123'
}
json_data = json.dumps(data)

r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)
