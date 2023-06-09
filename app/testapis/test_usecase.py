from datetime import datetime
import requests
query_use_case={
"usecase_id": 3,
    "created_by": "testuser",
    "created_on": str(datetime.now()),
    "updated_by": "testuser",
    "updated_on": str(datetime.now()),
    "use_case_description":"person detection",
    "usecase_name": "person detection"
}
url="http://localhost:8000/insertUsecase"
resp=requests.post(url,json=query_use_case)
print(resp.json())