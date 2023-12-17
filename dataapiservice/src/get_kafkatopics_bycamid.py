class GetKafkaDataByCamid():
    def get_data(connection,camera_id):
        # if camera_group_id is None:
        print("=====kfka topic=====",camera_id)
        if camera_id is not None and len(camera_id)==1:
                camera_id=str(camera_id).replace(',','')
        query=f"""
            SELECT distinct(cm.camera_id), topic_name FROM kafka_topics kt
inner join camera_master cm on cm.camera_id=kt.camera_id
inner join zone_master zm on zm.zone_id=cm.zone_id
inner join subsite_master sbm on sbm.subsite_id=zm.subsite_id
inner join location_master lm on lm.location_id=sbm.location_id
inner join schedule_master sm on sm.location_id=lm.location_id
where sm.is_deleted=0 and cm.is_deleted=0 and sm.status=1 and sm.is_deleted=0 and kt.is_deleted=0 and   kt.camera_id in {camera_id}
        """
        query1=f"""
           SELECT distinct(cm.camera_id), topic_name FROM kafka_topics kt
inner join camera_master cm on cm.camera_id=kt.camera_id
inner join zone_master zm on zm.zone_id=cm.zone_id
inner join subsite_master sbm on sbm.subsite_id=zm.subsite_id
inner join location_master lm on lm.location_id=sbm.location_id
inner join schedule_master sm on sm.location_id=lm.location_id
where sm.is_deleted=0 and cm.is_deleted=0 and sm.status=1 and sm.is_deleted=0 and kt.is_deleted=0"""
    
        if camera_id is None:
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
        


    
