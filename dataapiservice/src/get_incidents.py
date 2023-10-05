class GetIncidentData():
    def get_data(connection,usecase_id):
        query="""
            SELECT im.incident_id, im.incident_description, im.incident_name, im.incident_description,
im.incident_name, im.measurement_unit, im.incident_type_id, im.usecase_template_id,
icl.class_id, cm.class_name, uil.usecase_id, it.incident_type_id, it.incident_type_name, com.computation_name, com.tolerance,
com.upper_limit, com.lower_limit
                FROM `tcl-dev`.incident_master im
                left join incident_class_link icl on icl.incident_id=im.incident_id
                left join class_master cm on icl.class_id=cm.class_id
                left join usecase_incident_link uil on uil.incident_id=im.incident_id
                left join incident_type it on it.incident_type_id=im.incident_type_id
                left join computation com on com.incident_id= im.incident_id
                
            where  cm.is_deleted=0 and im.is_deleted=0 and it.is_deleted=0 
            and uil.usecase_id= %s
        """

        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (usecase_id,))
            column_names = [i[0] for i in cur.description]

            for i in cur:
                dictdata={}
                dictdata["incident_id"]=i[column_names.index('incident_id')] 
                dictdata["incident_name"]=i[column_names.index('incident_name')] 
                dictdata["measurement_unit"] = i[column_names.index('measurement_unit')] 
                dictdata["incident_type_id"]=i[column_names.index('incident_type_id')] 
                dictdata["incident_type_name"]=i[column_names.index('incident_type_name')]
                dictdata["class_id"]=i[column_names.index('class_id')]
                dictdata["class_name"]=i[column_names.index('class_name')] 
                dictdata["computation_name"]=i[column_names.index('computation_name')] 
                dictdata["upper_limit"]=i[column_names.index('upper_limit')] 
                dictdata["lower_limit"]=i[column_names.index('lower_limit')] 
                dictdata["tolerance"]=i[column_names.index('tolerance')] 
                listresult.append(dictdata)
            
            
        return {"data":listresult}        
        


    
