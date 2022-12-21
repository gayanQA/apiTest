import json
import requests

request_body = open("data.json", "r").read()
respon = requests.post("https://reqres.in/api/users", data=json.loads(request_body))
print(respon.json())
assert respon.json()['job'] == "QE" and respon.json()['name'] == 'Gayan'