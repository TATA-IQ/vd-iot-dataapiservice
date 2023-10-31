class GetModelConfigById():

    def get_data(connection,model_id,location_id=None,logger=None):

        """

        Retrieves model config filtered data from the 'tcom_model_config' table based on the provided 'model_id' and

        'location_id'.

 

        Args:

            connection: MySQL connection object.

            model_id:

            location_id:

 

        Returns:

            A dictionary of model config.

        """

        if location_id!=None:

            query="select * from tcom_model_config where model_id=%s and location_id=%s"

        else:

            query="select * from tcom_model_config where model_id=%s"

           

       

       

        listresult=[]

        with connection.cursor() as cur:

            res=[]

            if location_id!=None:

                cur.execute(query, (model_id,location_id,))

            else:

                cur.execute(query, (model_id,))

            for i in cur:

                    #print()

                dictdata={}

                dictdata["model_config_id"]=i[0]

                dictdata["agnostic_nms"]=i[1]

                dictdata["augment"]=i[2]

                dictdata["conf_thres"]=i[3]

                dictdata["half"]=i[6]

                dictdata["imgsz"]=i[7]

                dictdata["iou_thres"]=i[8]

                dictdata["location_id"]=i[12]

                dictdata["model_id"]=i[13]

               

               

                listresult.append(dictdata)

 

 

        return {"data":listresult}