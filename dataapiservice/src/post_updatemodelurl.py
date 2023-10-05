class UpdateEndPoint():
    def update(cnx,model_end_point,model_id,logger=None):
        query="update model set  model_url=%s where model_id=%s"
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                cur.execute(query, (model_end_point,model_id))
                cnx.commit()
            return {"data":"Model end point updated"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}