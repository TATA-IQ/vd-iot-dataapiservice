import requests
url=" http://172.16.0.178:8050/preview"
# url=" http://localhost:9005/preview"
# json_preview={"rtsp_url":"rtsp://14.142.72.131:554/live.sdp", "username" : "admin", "password":"Tata_123"}
json_preview={"rtsp_url":"rtsp://172.16.0.203:9097/human_counting", "username" : "", "password":""}

response=requests.get(url,json=json_preview)
print(response.json())