import requests
url=" http://172.16.0.205:8000/preview"
# url=" http://localhost:9005/preview"
# json_preview={"rtsp_url":"rtsp://14.142.72.131:554/live.sdp", "username" : "admin", "password":"Tata_123"}
# json_preview={"rtsp_url":"rtsp://172.16.0.203:9097/human_counting", "username" : "", "password":""}
json_preview={"rtsp_url":'rtsp://172.16.0.202:9097/pop', "username" : "", "password":""}

response=requests.post(url,json=json_preview)
print(response.json())