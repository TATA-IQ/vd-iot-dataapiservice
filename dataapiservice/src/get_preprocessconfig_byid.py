import fastapi
class GetPreProcessConfigDataById():
    def get_data(connection,preprocess_id=None,logger=None):
        """
        Retrives preprocess configuration data based on the given arguements and joining tcom_preprocess_config,
        tcom_preprocessing_master, tcom_processing_mapping, tcom_use_case, tcom_camera_group_list,

        Args:
            connection (object): mysql connection.
            camera_group_id (int) : provide the camera_group_id to filterdata based on it

        Returns:
            fastAPI JSONResponse which has preprocess configuration data.
        """
        
        if preprocess_id is not None and len(preprocess_id)==1:
                preprocess_id=str(preprocess_id).replace(',','')

        query1=f"""SELECT * FROM schedule_master sm
                left join  pre_process pp on sm.preprocess_id=pp.id
                inner join usecase uc on sm.usecase_id=uc.usecase_id
                
                where  sm.is_deleted=0 and uc.is_deleted=0 and 
                pp.id in {preprocess_id}"""
        
        if camera_group_id is None:
            query=query2
        else:
            query=query1
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            if cur.description is None:
                return  fastapi.responses.JSONResponse(content={"data":{},"error":"Please check params"})
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            print(len(resultset))
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    
                    dictdata["preprocess_id"]=i[column_names.index('preprocess_id')]
                    dictdata["description"]=i[column_names.index('description')]
                    
                    dictdata["brightness"]=i[column_names.index('brightness')]
                    dictdata["contrast_alpha"]=i[column_names.index('contrast_alpha')]
                    dictdata["contrast_beta"]=i[column_names.index('contrast_beta')]
                    dictdata["timezone_offset"]=i[column_names.index('timezone_offset')]
                    dictdata["contrast_sigma_one"]=i[column_names.index('contrast_sigma_one')]
                    dictdata["contrast_sigma_two"]=i[column_names.index('contrast_sigma_two')]

                    dictdata["roi"]=i[column_names.index('roi')]

                    dictdata["orientation_degree"]=i[column_names.index('orientation_degree')]
                    dictdata["image_height"]=i[column_names.index('image_height')]
                    dictdata["image_width"]=i[column_names.index('image_width')]
                    #dictdata["mask_image"]=i[column_names.index('mask_image')]
                    #dictdata["split"]=i[column_names.index('split')]
                    dictdata["split_process_column"]=i[column_names.index('split_process_column')]
                    dictdata["split_process_column_size"]=i[column_names.index('split_process_column_size')]
                    dictdata["split_process_row"]=i[column_names.index('split_process_row')]
                    dictdata["split_process_row_size"]=i[column_names.index('split_process_row_size')]
                    
                    #dictdata["threshold"]=i[column_names.index('threshold')]
                    #dictdata["preprocess_name"]=i[column_names.index('preprocess_name')]
                    #dictdata["preprocess_type"]=i[column_names.index('preprocess_type')]
                    dictdata["scheduling_id"]=i[column_names.index('id')]
                    dictdata["usecase_id"]=i[column_names.index('usecase_id')]
                    dictdata["usecase_name"]=i[column_names.index('usecase_name')]
                    #dictdata["input_process_id"]=i[column_names.index('input_process_id')]
                    
                    
                    listresult.append(dictdata)

        # print(listresult)
        return fastapi.responses.JSONResponse(content={"data":listresult})


       