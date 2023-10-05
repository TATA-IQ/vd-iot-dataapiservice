import requests
url=" http://127.0.0.1:8000/getScheduleMaster"
json_customer={"camera_group_id":["1","2","3"]}
response=requests.get(url,json=json_customer)
print(response.json())
