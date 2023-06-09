import sqlalchemy
import pandas as pd
class GetModelMaster():
    def get_data(connection,logger=None):
        
        query="select * from tcom_model_master"
        
        
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
            if len(resultset)>0:
                for i in resultset:
                    #print()
                    dictdata={}
                    dictdata["model_id"]=i[0]
                    dictdata["model_name"]=i[1]
                    dictdata["model_type"]=i[3]
                    dictdata["model_framework"]=i[4]
                    dictdata["usecase_id"]=i[5]
                    dictdata["model_endpoint"]=i[6]
                    
                    listresult.append(dictdata)


        return {"data":listresult}

class GetModelMasterById():
    def get_data(connection,model_id,logger=None):
        
        query="select * from tcom_model_master where model_id=%s"
        
        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (model_id,))
            for i in cur:
                    #print()
                dictdata={}
                dictdata["model_id"]=i[0]
                dictdata["batchsize"]=i[1]
                dictdata["device"]=i[4]
                dictdata["model_framework"]=i[7]
                dictdata["model_type"]=i[9]
                
                
                listresult.append(dictdata)


        return {"data":listresult}
