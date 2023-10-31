class GetPostProcessConfigData():
    def get_data(connection,usecase_id=None,logger=None):
        """
        Retrives preprocess configuration data based on the given arguements and joining tcom_preprocess_config,
        tcom_preprocessing_master, tcom_processing_mapping, tcom_use_case, tcom_camera_group_list,

        Args:
            connection (object): mysql connection.
            camera_group_id (int) : provide the camera_group_id to filterdata based on it

        Returns:
            fastAPI JSONResponse which has preprocess configuration data.
        """
        
        # if camera_group_id is not None and len(camera_group_id)==1:
        #         camera_group_id=str(camera_group_id).replace(',','')
        print("------",usecase_id)
        if usecase_id is not None and len(usecase_id)==1:
            usecase_id=str(usecase_id).replace(',','')
        print("+++++",usecase_id)
                
        query=f"""select pp.id,pp.image_size_height, pp.image_size_width, pp.legend, pp.name, pp.usecase_id,
                uc.usecase_id, uc.usecase_name, uc.usecase_description, uc.usecase_template_id,
                us.id, uts.step_name, uts.step_type, uts.step_no,us.computation_id, us.model_id model_id
                from post_process pp               
                inner join usecase uc on uc.usecase_id=pp.usecase_id
                inner join usecase_template ut on uc.usecase_template_id=ut.id
                inner join usecase_template_step uts on uts.usecase_template_id=ut.id
                inner join usecase_step us on uts.id=us.usecase_template_step_id and us.usecase_id=uc.usecase_id
                where uc.usecase_id in {usecase_id}
                """
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query)
            column_names = [i[0] for i in cur.description]

            for i in cur:
                dictdata={}
                dictdata["postprocess_id"]=i[column_names.index('id')]
                dictdata["image_height"]=i[column_names.index('image_size_height')] 
                dictdata["image_width"]=i[column_names.index('image_size_width')] 
                dictdata["legend"] = i[column_names.index('legend')] 
                dictdata["postprocess_name"]=i[column_names.index('name')] 
                #dictdata["schedule_status"]=i[column_names.index('status')]
                dictdata["usecase_id"]=i[column_names.index('usecase_id')]
                dictdata["usecase_name"]=i[column_names.index('usecase_name')] 
                dictdata["usecase_description"]=i[column_names.index('usecase_description')] 
                dictdata["usecase_template_id"]=i[column_names.index('usecase_template_id')]
                dictdata["usecase_step_id"]=i[column_names.index('id')] 
                dictdata["step_name"]=i[column_names.index('step_name')] 
                dictdata["step_no"]=i[column_names.index('step_no')] 
                dictdata["step_type"]=i[column_names.index('step_type')]
                dictdata["computation_id"]=i[column_names.index('computation_id')]
                dictdata["model_id"]=i[column_names.index('model_id')]
                dictdata["model_id"]=i[column_names.index('model_id')]
                listresult.append(dictdata)
        return {"data":listresult}  
        
        # query=f"""select pp.id,pp.image_size_height, pp.image_size_width, pp.legend, pp.name, pp.usecase_id,

        #          uc.usecase_id, uc.usecase_name, uc.usecase_description, uc.usecase_template_id,

        #         us.id, uts.step_name, uts.step_type, us.computation_id, us.model_id model_id

        #         from post_process pp               

        #         inner join usecase uc on uc.usecase_id=pp.usecase_id

        #         inner join usecase_template ut on uc.usecase_template_id=ut.id

        #         inner join usecase_template_step uts on uts.usecase_template_id=ut.id

        #         inner join usecase_step us on uc.usecase_id=us.usecase_id 

        #         where uc.usecase_id in {usecase_id} and uts.step_no=2

        #         """
        # print(query)
        # listresult=[]
        # with connection.cursor() as cur:
        #     res=[]
        #     cur.execute(query)
        #     column_names = [i[0] for i in cur.description]

        #     for i in cur:
        #         dictdata={}
        #         dictdata["postprocess_id"]=i[column_names.index('id')]
        #         dictdata["image_height"]=i[column_names.index('image_size_height')] 
        #         dictdata["image_width"]=i[column_names.index('image_size_width')] 
        #         dictdata["legend"] = i[column_names.index('legend')] 
        #         dictdata["postprocess_name"]=i[column_names.index('name')] 
        #         #dictdata["schedule_status"]=i[column_names.index('status')]
        #         dictdata["usecase_id"]=i[column_names.index('usecase_id')]
        #         dictdata["usecase_name"]=i[column_names.index('usecase_name')] 
        #         dictdata["usecase_description"]=i[column_names.index('usecase_description')] 
        #         dictdata["usecase_template_id"]=i[column_names.index('usecase_template_id')]
        #         dictdata["usecase_step_id"]=i[column_names.index('id')] 
        #         # dictdata["step_name"]=i[column_names.index('step_name')] 
        #         dictdata["step_name"]=i[column_names.index('step_name')] 
        #         # dictdata["step_no"]=i[column_names.index('step_no')] 
        #         dictdata["step_no"]=2 
        #         dictdata["step_type"]=i[column_names.index('step_type')]
        #         dictdata["computation_id"]=i[column_names.index('computation_id')]
        #         dictdata["model_id"]=i[column_names.index('model_id')]
        #         dictdata["model_id"]=i[column_names.index('model_id')]
        #         listresult.append(dictdata)
        # return {"data":listresult}  
        
              
                



