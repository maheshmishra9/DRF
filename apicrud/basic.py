import requests
import json


URL = "http://localhost:8000/class/based/crud/category/"

def get_data(id = None):
    data = {}

    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
get_data(16)

def post_data():
    data = {
        "name":"classbased",
        "description":"My name is mahesh mishra",
        "category_id":"mah11"
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
    
# post_data()

def update_data():
    data = {
        "id":"13",
        "name":"lastfyguht",
        "description":"last description",
        "category_id":"id"
        
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {
        "id":"3"
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data = json_data)
    data = r.json()
    print(data)
# delete_data()



