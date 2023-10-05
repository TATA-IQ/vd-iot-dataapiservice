class GetBoundaryData():
    def get_data(connection,usecase_id):
        #where bg.usecase_id=%s
        
        if usecase_id is not None and len(usecase_id)==1:
            
            usecase_id=str(usecase_id).replace(',','')
            # print("++++",test_id)
        
        query=f"""
            SELECT b.boundary_id, b.boundary_group_id, b.color, bc.boundary_coordinates_id, bc.x_coordinate,
            bc.y_coordinate, bg.processing_stage, bg.status, bg.camera_id, bg.incident_id, bg.usecase_id
            FROM `tcl-dev`.post_process_boundary ppb
            inner join boundary b on ppb.boundary_id=b.boundary_id
            inner join boundary_group bg on bg.boundary_group_id=b.boundary_group_id
            inner join boundary_coordinates bc on bc.boundary_id=b.boundary_id 
            where bg.usecase_id in {usecase_id}"""
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            print("---------")

            for i in cur:
                dictdata={}
                dictdata["boundary_id"]=i[column_names.index('boundary_id')] 
                dictdata["boundary_group_id"]=i[column_names.index('boundary_group_id')] 
                dictdata["color"] = i[column_names.index('color')] 
                dictdata["boundary_coordinates_id"]=i[column_names.index('boundary_coordinates_id')] 
                dictdata["x_coordinate"]=i[column_names.index('x_coordinate')]
                dictdata["y_coordinate"]=i[column_names.index('y_coordinate')]
                dictdata["status"]=i[column_names.index('status')] 
                dictdata["processing_stage"]=i[column_names.index('processing_stage')] 
                dictdata["camera_id"]=i[column_names.index('camera_id')]
                dictdata["incident_id"]=i[column_names.index('incident_id')] 
                dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                listresult.append(dictdata)
        return {"data":listresult}        
        


    
