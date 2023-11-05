import requests
url="http://172.16.0.204:8051/updateincidentvideoconf"
json_customer={"incident_video_id":"1",
                        "status":0,
                        "message":"in progress"}
response=requests.post(url,json=json_customer)
print(response.json())