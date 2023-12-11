class GetOnline:
    def get_data(connection,model_id=None,logger=None):
        
        query='''SELECT oul.online_file_id, oul.is_deleted, oul.file_name, oul.file_type, oul.online_id,
                ol.online_name, ol.url, ol.password, ol.user_id, 
                sm.id as schedule_id,sm.preprocess_id, sm.postprocess_id, sm.usecase_id,
                zm.zone_id, zm.zone_name, sbm.subsite_id, sbm.subsite_name, 
                lm.location_id, lm.location_name, cm.customer_id, cm.customer_name,
                ctm.city_id,ctm.name,
                cam.camera_id, cam.camera_name, cam.fps, cam.image_height, cam.image_width,cam.is_deleted,
                kt.topic_id, kt.topic_name, kt.processing_stage, kt.kafka_id, kt.partition_id

                FROM online_upload_list oul
                inner join online ol on oul.online_id=ol.online_id
                inner join camera_master cam on ol.zone_id=cam.zone_id
                inner join schedule_master sm on sm.online_id=ol.online_id
                inner join zone_master zm on ol.zone_id= zm.zone_id
                inner join subsite_master sbm on sbm.subsite_id=zm.subsite_id
                inner join location_master lm on lm.location_id=sbm.location_id
                inner join customer_master cm on cm.customer_id= lm.customer_id

                inner join city_master ctm on lm.city_id=ctm.city_id and ctm.customer_id=cm.customer_id
                inner join kafka_topics kt on kt.camera_id=cam.camera_id 
                where cam.is_dummy=1 and sm.status=1 and cam.is_deleted=0
            '''


                    dictdata["online_file_id"]=i[column_names.index('online_file_id')]
                    dictdata["file_name"]=i[column_names.index('file_name')]
                    dictdata["file_type"]=i[column_names.index('file_type')]
                    dictdata["online_id"]=i[column_names.index('online_id')]
                    dictdata["online_name"]=i[column_names.index('online_name')]
                    dictdata["url"]=i[column_names.index('url')]
                    dictdata["password"]=i[column_names.index('password')]

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
                    dictdata["password"]=i[column_names.index('password')]
                    dictdata["rtsp_url"]=i[column_names.index('url')]
                    dictdata["subsite_id"]=i[column_names.index('subsite_id')]
                #     dictdata["city_id"]=i[column_names.index('city_id')]
                    dictdata["user"]=i[column_names.index('user_id')]
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
                    
        

