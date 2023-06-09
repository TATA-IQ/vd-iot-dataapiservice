
import pandas as pd

from multipledispatch import dispatch
class GetClassMaster():
    
    def get_data(connection,logger=None):
        query="select * from tcom_class_master "
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    dictdata["class_id"]=i[0]
                    dictdata["class_name"]=i[1]
                    listresult.append(dictdata)

        return {"data":listresult}
    '''
    def get_data(connection,logger=None):
        query="select * from tcom_class_master "
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    dictdata["class_id"]=i[0]
                    dictdata["class_name"]=i[1]
                    listresult.append(dictdata)

        return {"data":listresult}
        '''