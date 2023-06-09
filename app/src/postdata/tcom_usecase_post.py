class Tcom_Usecase_Insert():
    def insert(cnx,data):
        query="insert into tcom_use_case(usecase_id,created_by,created_on,updated_by,updated_on,use_case_description,usecase_name) values(%s,%s,%s,%s,%s,%s,%s)"
        try:
            with cnx.cursor() as cur:
                print("Inseting")
                cur.execute(query, (data.usecase_id,data.created_by,data.created_on,data.updated_by,data.updated_on,data.use_case_description,data.usecase_name))
                cnx.commit()
            return {"data":"Inserted into Usecase table"}
        except Exception as ex:
            return {"data":ex}
