
import requests
query={
    "container_name":"cn1",
    "container_tag":"cn1",
    "model_id":2,
    "model_usecase":"person",
    "model_path":"/model/tensorflow/Person.zip",
    "model_port":"5000",
    "model_framework":"tensorflow",
    "model_name":"Person.zip"
}
url="http://localhost:8000/insertContainerModel"
resp=requests.post(url,json=query)
print(resp.json())