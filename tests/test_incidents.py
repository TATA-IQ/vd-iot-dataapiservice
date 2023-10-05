import requests
url=" http://localhost:8000/getincidents"
json_customer={"usecase_id":"7"}
response=requests.get(url,json=json_customer)
print(response.json())