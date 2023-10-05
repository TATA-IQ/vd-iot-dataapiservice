class UpdateModelPort():
    def update(cnx,model_port,model_id,logger=None):
        query="""update port_model set  model_id=%s, used_status=1 where port_number=%s"""
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                print(query)
                cur.execute(query, (model_id,model_port,))
                cnx.commit()
            return {"data":"Update portnumber for model"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}