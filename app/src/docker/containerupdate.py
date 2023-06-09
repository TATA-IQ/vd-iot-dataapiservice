class UpdateContainer():
    def update(cnx,container_id,container_name,logger=None):
        print("updating======")
        query="update tcom_container set  container_id=%s where container_name=%s"
        try:
            with cnx.cursor() as cur:
                cur.execute(query, (container_id,container_name))
                cnx.commit()
            return {
                "data":"success"
            }
        except Exception as ex:
            return {
                "data":ex
            }
