import requests
url=" http://localhost:8000/ports"
json_customer={"usecase_id":"1"}
response=requests.get(url,json={})
print(response.json())