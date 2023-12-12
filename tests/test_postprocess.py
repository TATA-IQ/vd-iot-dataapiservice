import requests
url=" http://localhost:8000/getpostprocess"
json_customer={"camera_group_id":"1"}
response=requests.get(url,json=json_customer)
print(response.json())