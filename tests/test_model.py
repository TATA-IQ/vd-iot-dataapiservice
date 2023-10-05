import requests
url=" http://localhost:8000/getModelMasterbyId"
json_customer={"model_id":"1"}
response=requests.get(url,json=json_customer)
print(response.json())