class GetModelMasterById():
    def get_data(connection,model_id,logger=None):
        """ 
        Retrives model master data by filtering the model table bases on provided model_id
        Args:
            connection (object): mysql connection object
            model_id (int): model_id for which model master data is needed
        Returns:
            Model master data
        """
        
        query="""select * from model m inner join
         framework f on m.framework_id=f.framework_id 
         inner join model_type mt on mt.model_type_id = m.model_type_id
         where model_id=%s and m.status=1"""
        
        

        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (model_id,))
            column_names = [i[0] for i in cur.description]
            for i in cur:
                    #print()
                dictdata={}
                dictdata["model_id"]=i[column_names.index('model_id')] 
                dictdata["model_name"]=i[column_names.index('model_name')] 
                dictdata["model_type"]=i[column_names.index('model_type_name')] 
                dictdata["model_framework"]=i[column_names.index('framework_name')] 
                # dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                dictdata["model_endpoint"]=i[column_names.index('model_url')] 
                dictdata["model_path"]=i[column_names.index('model_path')] 
                # dictdata["device"]=i[column_names.index('device')]
                
                
                listresult.append(dictdata)


        return {"data":listresult}
