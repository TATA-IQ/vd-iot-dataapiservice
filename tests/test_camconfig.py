import requests
url=" http://127.0.0.1:8000/getCameraConfig"
response=requests.get(url,json={"camera_group_id":["1"]})
print(response.json())