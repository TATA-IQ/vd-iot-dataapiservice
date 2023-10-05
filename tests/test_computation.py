import requests
url=" http://localhost:8000/getcomputation"
json_customer={"usecase_id":"2"}
response=requests.get(url,json=json_customer)
print(response.json())