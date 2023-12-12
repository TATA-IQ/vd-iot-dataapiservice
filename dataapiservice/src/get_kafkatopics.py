class GetKafkaData():
    def get_data(connection,camera_group_id):
        # if camera_group_id is None:
        print("=====kfka topic=====",camera_group_id)
        if camera_group_id is not None and len(camera_group_id)==1:
                camera_group_id=str(camera_group_id).replace(',','')
        query=f"""
            SELECT distinct(cm.camera_id), topic_name FROM kafka_topics kt
inner join camera_master cm on cm.camera_id=kt.camera_id
inner join camera_group_list cgl on cgl.camera_id=cm.camera_id and cgl.camera_id=kt.camera_id
inner join camera_group cg on cg.camera_group_id=cgl.camera_group_id
inner join schedule_master sm on sm.camera_group_id=cg.camera_group_id
where sm.is_deleted=0 and cm.is_deleted=0 and cg.is_deleted=0 and cgl.is_deleted=0 and  cg.camera_group_id in {camera_group_id}
        """
        query1=f"""
            SELECT distinct(cm.camera_id), topic_name FROM kafka_topics kt
inner join camera_master cm on cm.camera_id=kt.camera_id
inner join camera_group_list cgl on cgl.camera_id=cm.camera_id and cgl.camera_id=kt.camera_id
inner join camera_group cg on cg.camera_group_id=cgl.camera_group_id
inner join schedule_master sm on sm.camera_group_id=cg.camera_group_id
where sm.is_deleted=0 and cm.is_deleted=0 and cg.is_deleted=0 and cgl.is_deleted=0"""
        if camera_group_id is None:
            query=query1 
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query)
            column_names = [i[0] for i in cur.description]

            for i in cur:
                dictdata={}
                dictdata["camera_id"]=i[column_names.index('camera_id')] 
                dictdata["topic_name"]=i[column_names.index('topic_name')] 
                listresult.append(dictdata)
        return {"data":listresult}        
        


    
