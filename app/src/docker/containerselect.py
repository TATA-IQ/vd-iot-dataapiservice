class ExistContainerByName():
    def get_data(cnx,container_nm,logger=None):
        print("name====>",container_nm)
        query=("select * from tcom_container"
        " where container_name=%s")
        boolstatus=False
        with cnx.cursor() as cur:
            res=[]
            cur.execute(query, (container_nm,))
            for i in cur:
                
            
                boolstatus=True
                break
            
        return {"data":boolstatus}
class ExistContainerModelByName():
    def get_data(cnx,container_nm,logger=None):
        print("name====>",container_nm)
        query=("select * from tcom_container_model"
        " where container_name=%s")
        boolstatus=False
        with cnx.cursor() as cur:
            res=[]
            cur.execute(query, (container_nm,))
            for i in cur:
                
            
                boolstatus=True
                break
            
        return {"data":boolstatus}

class ExistContainerById():
    def get_data(cnx,container_id,logger=None):
        print("name====>",container_id)
        query=("select * from tcom_container"
        " where container_id=%s")
        boolstatus=False
        with cnx.cursor() as cur:
            res=[]
            cur.execute(query, (container_nm,))
            for i in cur:
                
            
                boolstatus=True
                break
            
        return {"data":boolstatus}

class GetContainerByContainerid():
    def get_data(cnx,container_id,logger=None):
        print("name====>",container_id)
        query=("select * from tcom_container"
        " where container_id=%s")
        boolstatus=False
        listresult=[]
        #container_id varchar(64),container_name varchar(64), container_tag varchar(64),model_id varchar(64)
        with cnx.cursor() as cur:
            res=[]
            cur.execute(query, (container_id,))
            for i in cur:
                dicres={}
                dicres["container_id"]=i[0]
                dicres["container_name"]=i[1]
                dicres["container_tag"]=i[2]
                dicres["model_id"]=i[3]
                listresult.append(dicres)
           
        return {"data":listresult}

class GetContainerModelByModelId():
    #container_name, container_tag, model_id, model_usecase, model_path,model_port,model_framework,model_name
    def get_data(cnx,model_id,logger=None):
        print("name====>",model_id)

        query=("select * from tcom_container_model"
        " where model_id=%s")
        boolstatus=False
        listresult=[]
        with cnx.cursor() as cur:
            
            cur.execute(query, (model_id,))
            for i in cur:
                res={}
                res["container_name"]=i[0]
                res["container_tag"]=i[1]
                res["model_id"]=i[2]
                #res["model_usecase"]=i[3]
                res["model_path"]=i[3]
                res["model_port"]=i[4]
                #res["model_framework"]=i[6]
                res["file_name"]=i[5]
                listresult.append(res)

                #res={}


                
            
                
            
        return {"data":listresult}

class GetContainerModel():
    
    def get_data(cnx,logger=None):
        query="select * from tcom_container_model "
        print(query)
        listresult=[]
        with cnx.cursor() as cur:
            cur.execute(query)
            resultset=cur.fetchall()
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    dictdata["container_name"]=i[0]
                    dictdata["container_tag"]=i[1]
                    dictdata["model_id"]=i[2]
                    dictdata["model_name"]=i[3]
                    dictdata["model_path"]=i[4]
                    listresult.append(dictdata)

        return {"data":listresult}
