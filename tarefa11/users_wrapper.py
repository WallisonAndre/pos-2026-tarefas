import requests

url_base = "https://jsonplaceholder.typicode.com/users"

def list():
    r = requests.get(url_base)
    return r.json()

def read(user_id):
    r = requests.get(url_base + "/" + str(user_id))
    return r.json()

def create(user_data):
    r = requests.post(url_base, json=user_data)
    return r.json()

def update(user_id, user_data):
    r = requests.put(url_base + "/" + str(user_id), json=user_data)
    return r.json()

def delete(user_id):
    r = requests.delete(url_base + "/" + str(user_id))
    if r.status_code == 200:
        return True
    return False