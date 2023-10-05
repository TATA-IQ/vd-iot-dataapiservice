class GetPortDetails():
    def get_data(connection,model_id=None,logger=None):
        """ 
        Retrives port data by filtering the model table bases on provided model_id
        Args:
            connection (object): mysql connection object
            model_id (int): model_id for which model master data is needed
        Returns:
           Port Details
        """
        
        query="""select * from port_model where used_status=0"""
        query2= """select * from port_model where used_status=1 and model_id=%s"""
        
        print("====called---")
        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            if model_id is not None:
                print("query====>",query)
                query=query2
                cur.execute(query, (model_id,))
            else:
                print("query====>",query)
                cur.execute(query)
            column_names = [i[0] for i in cur.description]
            print(column_names)
            for i in cur:
                    #print()
                dictdata={}
                dictdata["model_id"]=i[column_names.index('model_id')] 
                dictdata["port_number"]=i[column_names.index('port_number')] 
                dictdata["used_status"]=i[column_names.index('used_status')] 
                
                listresult.append(dictdata)


        return {"data":listresult}
