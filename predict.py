import requests

url = 'http://127.0.0.1:5000/predict_api'
r = requests.post(url,json={'link':0})

print(r.json())