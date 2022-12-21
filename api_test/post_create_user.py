import requests

request_body = {
                "name": "Gayan",
                "job": "QE"
}
respon = requests.post("https://reqres.in/api/users", data=request_body)
print(respon.json())
assert respon.json()['job'] == "QE" and respon.json()['name'] == 'Gayan'