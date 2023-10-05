class GetClassesData():
    def get_data(connection,usecase_id):
        query="""
            SELECT us.usecase_id,us.step_no,us.step_name, us.step_type,cm.class_name as uc_class_name, umc.conf as uc_class_conf,
            mcl.conf, mcl.uploaded_class_name, mcl.actual_class_id, cm.class_name, cm.class_description, mt.model_type_name, m.model_url,m.model_name, m.model_id,m.model_type_id,fw.framework_name, ppb.bound_color,ppb.bound_thickness,ppb.text_color, ppb.text_thickness 
            FROM `tcl-dev`.usecase_step us
            inner join usecase_model_conf umc on umc.usecase_step_id=us.id
            inner join model m on m.model_id=us.model_id 
            inner join framework fw on m.framework_id=fw.framework_id 
            inner join model_type mt on mt.model_type_id = m.model_type_id
            inner join model_class_link mcl on mcl.model_id=m.model_id and mcl.model_id=us.model_id
            inner join class_master cm on cm.class_id=mcl.actual_class_id and umc.class_id=cm.class_id
            inner join post_process_property ppb on ppb.bound_class_id=cm.class_id
            where umc.is_deleted=0 and m.is_deleted=0 and us.is_deleted=0 and m.status=1
            and us.usecase_id= %s
        """
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (usecase_id,))
            column_names = [i[0] for i in cur.description]

            for i in cur:
                dictdata={}
                dictdata["step_no"]=i[column_names.index('step_no')] 
                dictdata["step_name"]=i[column_names.index('step_name')] 
                dictdata["step_type"]=i[column_names.index('step_type')]
                dictdata["uc_class_name"]=i[column_names.index('uc_class_name')] 
                dictdata["uc_class_conf"] = i[column_names.index('uc_class_conf')] 
                dictdata["uploaded_class_name"]=i[column_names.index('uploaded_class_name')]
                dictdata["actual_class_id"]=i[column_names.index('actual_class_id')]
                dictdata["conf"]=i[column_names.index('conf')]
                dictdata["model_id"]=i[column_names.index('model_id')]
                dictdata["model_url"]=i[column_names.index('model_url')]
                dictdata["model_name"]=i[column_names.index('model_name')]
                dictdata["bound_color"]=i[column_names.index('bound_color')]
                dictdata["bound_thickness"]=i[column_names.index('bound_thickness')]
                dictdata["text_color"]=i[column_names.index('text_color')]
                dictdata["text_thickness"]=i[column_names.index('text_thickness')]
                dictdata["model_type_id"]=i[column_names.index('model_type_id')]
                dictdata["model_type"]=i[column_names.index('model_type_name')]
                dictdata["model_framework"]=i[column_names.index('framework_name')]
                
                listresult.append(dictdata)
                print(dictdata)
        return {"data":listresult}        
        


    
