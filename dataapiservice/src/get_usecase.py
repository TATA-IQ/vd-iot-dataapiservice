class GetUsecase():

    def get_data(connection,logger=None):

        """

        Retrieves Usecase
        'location_id'.

 

        Args:

            connection: MySQL connection object.

            model_id:

            location_id:

 

        Returns:

            A dictionary of model config.

        """
        
        

        query="select distinct(usecase_id) from schedule_master"
        listresult=[]
        dictdata={}

        with connection.cursor() as cur:

            res=[]

            
            cur.execute(query)
            column_names = [i[0] for i in cur.description]

            for i in cur:

                #print()

                
                if "usecase_id" in dictdata:

                    dictdata["usecase_id"].append(i[column_names.index('usecase_id')])
                else:
                    dictdata["usecase_id"]=[i[column_names.index('usecase_id')]]
        return {"data":dictdata}
