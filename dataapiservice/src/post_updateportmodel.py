class UpdateModelPort():
    def update(cnx,model_port,model_id):
        print("========in update model port=============")
        query="""update port_model set model_id=%s, used_status=1 where port_number=%s """
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                print(query, model_id, model_port)
                cur.execute(query, (model_id,model_port,))
                cnx.commit()
            return {"data":"Update portnumber for model"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}