import sqlalchemy
import pandas as pd
class GetModelFramework():
    def get_data(connection,logger=None):
        query="select * from tcom_model_framework"
        listresult=[]
        
        with connection.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
       
            if len(resultset)>0:
                for i in resultset:
                    #print()
                    dictdata={}
                    dictdata["model_id"]=i[0]
                    dictdata["model_framework"]=i[1]
                    listresult.append(dictdata)


        return {"data":listresult}
        