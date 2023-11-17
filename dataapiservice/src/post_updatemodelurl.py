class UpdateEndPoint():
    def update(cnx,model_end_point,model_id,logger=None):
        print("======== update end point===========")
        query="update model set  model_url=%s where model_id=%s"
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                cur.execute(query, (model_end_point,model_id))
                cnx.commit()
                print(query, (model_end_point,model_id))
            return {"data":"Model end point updated"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}
        
class UpdateModelStatus():
    def update(cnx,model_id, status, message):
        print("========in update model status=============")
        query="""update model set status=%s, status_message=%s where model_id=%s"""
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                print(query, status, message, model_id)
                cur.execute(query, (status, message, model_id))
                cnx.commit()
            return {"data":"Updated running status for model"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}