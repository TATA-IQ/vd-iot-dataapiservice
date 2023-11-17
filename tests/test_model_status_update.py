import requests
url=" http://localhost:8000/updatemodelstatus"
json_customer={"model_id":5, "status":0, "message":"test"}
response=requests.post(url,json=json_customer)
print(response.json())