class InsertContainer():
    def insert(cnx,data,logger=None):
        query="insert into tcom_container (container_id, container_name,container_tag,model_id) values(%s,%s,%s,%s)"
        try:
            with cnx.cursor() as cur:
                print("Inseting")
                cur.execute(query, (data.container_id,data.container_name,data.container_tag,data.model_id))
                cnx.commit()
            return {"data":"success"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}


class InsertContainerModel():
    def insert(cnx,data,logger=None):
        print("*****")
        query="insert into tcom_container_model (container_name, container_tag,model_id,model_path,model_port,file_name) values(%s,%s,%s,%s,%s,%s)"
        try:
            with cnx.cursor() as cur:
                print("===executing===")
                cur.execute(query, (data.container_name,data.container_tag,data.model_id,data.model_path,data.model_port,data.file_name))
                cnx.commit()
            return {"data":"success"}
        except Exception as ex:
            return {"data":ex}
        
