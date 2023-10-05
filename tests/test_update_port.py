import requests
url=" http://127.0.0.1:8000/updateports"
json_customer={"model_id":1,"model_port":6500}
response=requests.post(url,json=json_customer)
print(response.json())