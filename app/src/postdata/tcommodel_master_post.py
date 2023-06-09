class UpdateEndPoint():
    def update(cnx,model_end_point,model_id,logger=None):
        query="update tcom_model_master set  model_end_point=%s where model_id=%s"
        try:
            with cnx.cursor() as cur:
                print("Inseting")
                cur.execute(query, (model_end_point,model_id))
                cnx.commit()
            return {"data":"Model end point updated"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}

class Insert_Tcom_Model_Master():
    def insert(cnx,data):
        query="insert into tcom_model_master(model_id,batchsize,created_by,created_on,device,model_description,model_end_point,model_framework,model_name,model_type,updated_on,usecase_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            with cnx.cursor() as cur:
                print("Inseting")
                cur.execute(query, (data.model_id,data.batchsize,data.created_by,data.created_on,data.device,data.model_description,data.model_end_point,data.model_framework,data.model_name,data.model_type,data.updated_on,data.usecase_id))
                cnx.commit()
            return {"data":"Inserted into the model master table"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}

