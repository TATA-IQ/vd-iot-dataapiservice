import requests
url=" http://127.0.0.1:8000/getCameraGroup"
# response=requests.get(url,json={})
# print(response.json())

# json_customer={"customer_id":["1"]}
# response=requests.get(url,json=json_customer)
# print(response.json())

# json_customer={"subsite_id":["1"]}
# response=requests.get(url,json=json_customer)
# print(response.json())

# json_customer={"zone_id":["1"]}
# response=requests.get(url,json=json_customer)
# print(response.json())

json_customer={"location_id":["1"]}
response=requests.get(url,json=json_customer)
print(response.json())