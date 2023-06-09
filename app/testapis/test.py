import requests
import random

import pandas as pd
from datetime import datetime
fg=(random.randrange(20, 2000000, 16)) 
#df=pd.read_csv("testdf.csv")
url = 'http://127.0.0.1:8000/insertContainers'
url2="http://127.0.0.1:8000/existContainerName"
url3="http://127.0.0.1:8000/insertContainerModel"
url4="http://172.16.0.170:8000/containermodel"
#dfstr=Encoder.encode(df)
#print(dfstr)
#
# query={"intrusion_detect":dfstr}
query={"container_id":"1","container_name":"test","container_tag":"test","model_id":"2"}
query={"container_id":"1"}
query={
    "container_name":"cn1",
    "container_tag":"cn1",
    "model_id":"id1",
    "model_usecase":"person",
    "model_path":"/model/tensorflow/Person.zip",
    "model_port":"5000",
    "model_framework":"tensorflow",
    "model_name":"Person.zip"
}
query_model_master={
    "model_id": 2,
    "batchsize":  1,
    "createdby": "testuser",
    "created_on": str(datetime.now()),
    "device": "cpu",
    "model_description": "person detection",
    "model_end_point": "",
    "model_framework":"tensorflow",
    "model_name": "person",
    "model_type": "object_detection",
    "updated_on": datetime.now(),
    "usecase_id": 2

}
query_use_case={
"usecase_id": 3,
    "created_by": "testuser",
    "created_on": str(datetime.now()),
    "updated_by": "testuser",
    "updated_on": str(datetime.now()),
    "use_case_description":"person detection",
    "usecase_name": "person detection"
}

#r = requests.post(url3, json=query)
r = requests.get(url4, json={"model_id":"id2"})
data = r.json()
print(r.json())
# print(data,"\n")
