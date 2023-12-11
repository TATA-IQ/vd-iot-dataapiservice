import requests
url=" http://172.16.0.178:8001/getonline"
json_customer={"usecase_id":"1"}
response=requests.get(url)
print(response.json())