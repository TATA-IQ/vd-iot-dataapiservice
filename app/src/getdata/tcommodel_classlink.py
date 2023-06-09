import sqlalchemy
import fastapi
import pandas as pd
class GetModelClassLink():
    def get_data(connection,logger=None):
       
        query="select * from tcom_model_class_link"
    
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
            print(len(resultset))
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    dictdata["class_id"]=i[0]
                    dictdata["model_id"]=i[1]
                    

                    listresult.append(dictdata)

        print(listresult)
        return fastapi.responses.JSONResponse(content={"data":listresult})
        