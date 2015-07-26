post_url = 'http://localhost:8001/api/expense/'
post_data = {"Cost": 55.0, "Name": "Sim Card"}
headers = {'Content-type': 'application/json'}
import requests
import json
r = requests.post(post_url, json.dumps(post_data), headers=headers)
print r.status_code