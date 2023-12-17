class GetUpload:
    def get_data(connection,logger=None):
        
        query='''select u.upload_id, u.is_deleted, u.folder_name, u.path, u.series_id,
                u.parent_id,  
                sm.id as schedule_id,sm.preprocess_id, sm.postprocess_id, sm.usecase_id, uc.usecase_name,sm.timezone, sm.timezone_offset,
                zm.zone_id, zm.zone_name, sbm.subsite_id, sbm.subsite_name, 
                lm.location_id, lm.location_name, cm.customer_id, cm.customer_name,
                ctm.city_id,ctm.name,
                cam.camera_id, cam.camera_name, cam.fps, cam.image_height, cam.image_width,cam.is_deleted,
                kt.topic_id, kt.topic_name, kt.processing_stage, kt.kafka_id, kt.partition_id
				from  upload u
                inner join camera_master cam on u.zone_id=cam.zone_id
                inner join schedule_master sm on sm.upload_id=u.parent_id
                inner join usecase uc on uc.usecase_id=sm.usecase_id
                inner join zone_master zm on u.zone_id= zm.zone_id
                inner join subsite_master sbm on sbm.subsite_id=zm.subsite_id
                inner join location_master lm on lm.location_id=sbm.location_id
                inner join customer_master cm on cm.customer_id= lm.customer_id
                inner join city_master ctm on lm.city_id=ctm.city_id and ctm.customer_id=cm.customer_id
                inner join kafka_topics kt on kt.camera_id=cam.camera_id 
                where sm.status=1 and cam.is_dummy=1 and cam.is_deleted=0
            '''
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            for i in cur:

                dictdata={}
                dictdata["upload_id"]=i[column_names.index('upload_id')]
                dictdata["folder_name"]=i[column_names.index('folder_name')]
                dictdata["path"]=i[column_names.index('path')]
                dictdata["series_id"]=i[column_names.index('series_id')]
                dictdata["parent_id"]=i[column_names.index('parent_id')]
                dictdata["schedule_id"]=i[column_names.index('schedule_id')]
                dictdata["preprocess_id"]=i[column_names.index('preprocess_id')]
                dictdata["postprocess_id"]=i[column_names.index('postprocess_id')]
                dictdata["usecase_id"]=i[column_names.index('usecase_id')]
                dictdata["timezone"]=i[column_names.index('timezone')]
                dictdata["timezone_offset"]=i[column_names.index('timezone_offset')]

                dictdata["camera_group_id"]=None
                dictdata["camera_group_name"]=None
                dictdata["group_description"]=None
                dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                dictdata["location_id"]=i[column_names.index('location_id')]
                dictdata["camera_grouplist_id"]=None
                dictdata["camera_id"]=i[column_names.index('camera_id')]
                dictdata["camera_name"]=i[column_names.index('camera_name')]
                dictdata["fps"]=25
                dictdata["image_height"]=i[column_names.index('image_height')]
                dictdata["image_width"]=i[column_names.index('image_width')]
                dictdata["ip"]=None
                dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                dictdata["password"]=None
                dictdata["url"]=None
                dictdata["subsite_id"]=i[column_names.index('subsite_id')]
            #     dictdata["city_id"]=i[column_names.index('city_id')]
                dictdata["user"]=None
                dictdata["city"]=i[column_names.index('name')]
                dictdata["city_id"]=i[column_names.index('city_id')]
                #dictdata["site"]=i[column_names.index('site')]
                try:
                    dictdata["time_zone"]=i[column_names.index('time_zone')]
                except:
                    dictdata["time_zone"]=""
                dictdata["customer_id"]=i[column_names.index('customer_id')]
                dictdata["customer_name"]=i[column_names.index('customer_name')]
                dictdata["subsite_id"]=i[column_names.index('subsite_id')]
                dictdata["subsite_name"]=i[column_names.index('subsite_name')]
                dictdata["topic_id"]=i[column_names.index('topic_id')]
                dictdata["partition_id"]=i[column_names.index('partition_id')]
                dictdata["processing_stage"]=i[column_names.index('processing_stage')]
                #dictdata["tcom_kafka_topicscol"]=i[column_names.index('tcom_kafka_topicscol')]
                dictdata["topic_name"]=i[column_names.index('topic_name')]
                dictdata["kafka_id"]=i[column_names.index('kafka_id')]
                dictdata["location_name"]=i[column_names.index('location_name')]
                dictdata["zone_id"]=i[column_names.index('zone_id')]
                dictdata["zone_name"]=i[column_names.index('zone_name')]
                dictdata["usecase_id"]=i[column_names.index('usecase_id')]
                dictdata["usecase_name"]=i[column_names.index('usecase_name')]
                dictdata["type"]="online"
                listresult.append(dictdata)
        return {"data":listresult}
        
                    
        

