import sqlalchemy
import fastapi
import pandas as pd
class GetUseCase():
    def get_data(connection,logger=None):
       
        query="select * from tcom_use_case"
    
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
                    dictdata["usecase_id"]=i[0]
                    dictdata["usecase_name"]=i[1]
                    

                    listresult.append(dictdata)

        print(listresult)
        return fastapi.responses.JSONResponse(content={"data":listresult})
        