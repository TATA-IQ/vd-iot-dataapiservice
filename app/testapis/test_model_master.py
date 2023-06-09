
import requests
from datetime import datetime
query_model_master={
    "model_id": 4,
    "batchsize":  1,
    "created_by": "testuser",
    "created_on": str(datetime.now()),
    "device": "cpu",
    "model_description": "assets",
    "model_end_point": "",
    "model_framework":"yolov5",
    "model_name": "assets",
    "model_type": "object_detection",
    "updated_on": str(datetime.now()),
    "usecase_id": 2

}
url="http://localhost:8000/insertModelMaster"
resp=requests.post(url,json=query_model_master)
print(resp.json())