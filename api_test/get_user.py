import requests

para_value = {"page":2}
respon = requests.get("https://reqres.in/api/users", params=para_value)
print(respon)
responCode = respon.status_code
print(responCode)
assert responCode == 200 ,"Invalid status code "

json_response = respon.json()
print(json_response)

print('total_pages:',json_response['total_pages'])
assert json_response['total_pages'] == 2 , "Value doesn't match"

print('Email :', json_response['data'][0]['email'])
assert json_response['data'][0]['email'].endswith("reqres.in"), "Email format should be in proper format"

print('URL :', json_response['support']['url'])
