import sqlalchemy
import pandas as pd
class GetModelCamGroup():
    def get_data(connection,logger=None):
        metadata=sqlalchemy.MetaData()
        #print("<=====Inside select====>",engine)
        query="select * from tcom_model_cameragroup"
        
        print(query)
        
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
            if len(resultset)>0:
                for i in resultset:
                    #print()
                    dictdata={}
                    dictdata["model_cameragroup_id"]=i[0]
                    dictdata["model_conifg_id"]=i[1]
                    dictdata["camera_group_id"]=i[2]
                    

                    listresult.append(dictdata)


        return {"data":listresult}
        