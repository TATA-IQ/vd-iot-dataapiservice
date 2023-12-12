import requests
url=" http://localhost:8000/getclasses"
json_customer={"usecase_id":"1"}
response=requests.get(url,json=json_customer)
print(response.json())