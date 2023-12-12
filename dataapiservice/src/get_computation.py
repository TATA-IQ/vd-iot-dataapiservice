class GetComputationData():
    def get_data(connection,usecase_id):
        query="""
            select uc.usecase_id, uc.usecase_name, uts.step_no, uts.step_name, uts.step_type,
            cm.computation_id, cm.computation_name, cm.incident_id, cm.lower_limit, cm.tolerance, cm.upper_limit
            from usecase uc inner join usecase_template ut on uc.usecase_template_id=ut.id
            inner join usecase_template_step uts on uts.usecase_template_id=ut.id
            inner join usecase_step us on uts.id=us.usecase_template_step_id
            inner join computation cm on cm.computation_id=us.computation_id
            where cm.is_deleted=0 and uc.is_deleted=0 
            and uc.usecase_id= %s
        """
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (usecase_id,))
            column_names = [i[0] for i in cur.description]

            for i in cur:
                dictdata={}
                dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                dictdata["usecase_name"]=i[column_names.index('usecase_name')] 
                dictdata["step_no"] = i[column_names.index('step_no')] 
                dictdata["step_name"]=i[column_names.index('step_name')] 
                dictdata["step_type"]=i[column_names.index('step_type')]
                dictdata["computation_id"]=i[column_names.index('computation_id')]
                dictdata["computation_name"]=i[column_names.index('computation_name')] 
                dictdata["incident_id"]=i[column_names.index('incident_id')] 
                dictdata["lower_limit"]=i[column_names.index('lower_limit')]
                dictdata["tolerance"]=i[column_names.index('tolerance')] 
                dictdata["upper_limit"]=i[column_names.index('upper_limit')] 
                listresult.append(dictdata)
        return {"data":listresult}        
        
        # query="""
        #     select uc.usecase_id, uc.usecase_name, uts.step_no, uts.step_name, uts.step_type,
        #     cm.computation_id, cm.computation_name, cm.incident_id, cm.lower_limit, cm.tolerance, cm.upper_limit
        #     from usecase uc inner join usecase_template ut on uc.usecase_template_id=ut.id
        #     inner join usecase_template_step uts on uts.usecase_template_id=ut.id
        #     inner join usecase_step us on uc.usecase_id=us.usecase_id 
        #     inner join computation cm on cm.computation_id=us.computation_id
        #     where cm.is_deleted=0 and uc.is_deleted=0 
        #     and uc.usecase_id= %s and uts.step_no = 2
        # """
        # listresult=[]
        # with connection.cursor() as cur:
        #     res=[]
        #     cur.execute(query, (usecase_id,))
        #     column_names = [i[0] for i in cur.description]

        #     for i in cur:
        #         dictdata={}
        #         dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
        #         dictdata["usecase_name"]=i[column_names.index('usecase_name')] 
        #         dictdata["step_no"] = i[column_names.index('step_no')] 
        #         dictdata["step_name"]=i[column_names.index('step_name')] 
        #         dictdata["step_type"]=i[column_names.index('step_type')]
        #         dictdata["computation_id"]=i[column_names.index('computation_id')]
        #         dictdata["computation_name"]=i[column_names.index('computation_name')] 
        #         dictdata["incident_id"]=i[column_names.index('incident_id')] 
        #         dictdata["lower_limit"]=i[column_names.index('lower_limit')]
        #         dictdata["tolerance"]=i[column_names.index('tolerance')] 
        #         dictdata["upper_limit"]=i[column_names.index('upper_limit')] 
        #         listresult.append(dictdata)
        # return {"data":listresult}        
        


    
