import requests
url=" http://localhost:9005/getincidentvideoconf"
json_filter={"incident_video_id":"3"}
response=requests.get(url,json=json_filter)
print(response.json())