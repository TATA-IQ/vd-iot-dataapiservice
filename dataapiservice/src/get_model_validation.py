import requests
class ValidationModel():
    def get_data(config_Api,model_id,framework):
        try:
            url=config_Api[int(framework)]
        except Exception as ex:
            print("Exception in url: ",ex)
            return {"status":"Failed","message":"model framework error"}
        # responses=requests.post(url,json={"model_framework":framework,"model_type":model_type,"model_name":model_name,"model_path":path})
        responses=requests.post(url,json={"model_id":model_id})
        print("responses=====>", responses.json())
        return responses.json()

