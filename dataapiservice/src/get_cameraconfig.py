import fastapi
class GetCameraConfigData():
    def get_data(connection,camera_group_id=None,logger=None):
        if camera_group_id is not None and len(camera_group_id)==1:
                camera_group_id=str(camera_group_id).replace(',','')
        query1=f"""select * from camera_group cg 
                inner join camera_group_list cl on cg.camera_group_id = cl.camera_group_id 
                inner join camera_master cm on cl.camera_id = cm.camera_id 
                inner join zone_master zm on cm.zone_id=zm.zone_id
                inner join kafka_topics kt on kt.camera_id = cm.camera_id 
                inner join location_master lm on lm.location_id=cg.location_id 
                inner join city_master as ct on ct.city_id=lm.city_id
                inner join customer_master cu on lm.customer_id=cu.customer_id 
                inner join subsite_master sm on zm.subsite_id=sm.subsite_id 
                where sm.is_deleted=0 and cu.is_deleted=0 and lm.is_deleted=0 and kt.is_deleted=0 
                and zm.is_deleted=0 and cm.is_deleted=0 and cl.is_deleted=0 and cg.is_deleted=0
                and  cg.camera_group_id in {camera_group_id}"""
        
        query2=f"""select * from camera_group cg 
                inner join camera_group_list cl on cg.camera_group_id = cl.camera_group_id 
                inner join camera_master cm on cl.camera_id = cm.camera_id 
                inner join zone_master zm on cm.zone_id=zm.zone_id
                inner join kafka_topics kt on kt.camera_id = cm.camera_id 
                inner join location_master lm on lm.location_id=cg.location_id 
                inner join customer_master cu on lm.customer_id=cu.customer_id 
                inner join subsite_master sm on zm.subsite_id=sm.subsite_id 
                where sm.is_deleted=0 and cu.is_deleted=0 and lm.is_deleted=0 and kt.is_deleted=0 
                and zm.is_deleted=0 and cm.is_deleted=0 and cl.is_deleted=0 and cg.is_deleted=0"""

        if camera_group_id is None:
                query=query2
        else:
                query=query1
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
                    dictdata["camera_group_id"]=i[column_names.index('camera_group_id')] 
                    dictdata["camera_group_name"]=i[column_names.index('camera_group_name')]
                    dictdata["group_description"]=i[column_names.index('group_description')]
                    dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                    dictdata["location_id"]=i[column_names.index('location_id')]
                    dictdata["camera_grouplist_id"]=i[column_names.index('camera_grouplist_id')]
                    dictdata["camera_id"]=i[column_names.index('camera_id')]
                    dictdata["camera_name"]=i[column_names.index('camera_name')]
                    dictdata["fps"]=i[column_names.index('fps')]
                    dictdata["image_height"]=i[column_names.index('image_height')]
                    dictdata["image_width"]=i[column_names.index('image_width')]
                    dictdata["ip"]=i[column_names.index('ip')]
                    dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                    dictdata["password"]=i[column_names.index('password')]
                    dictdata["rtsp_url"]=i[column_names.index('rtsp_url')]
                    dictdata["subsite_id"]=i[column_names.index('subsite_id')]
                #     dictdata["city_id"]=i[column_names.index('city_id')]
                    dictdata["user"]=i[column_names.index('user')]
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
                    
                    listresult.append(dictdata)

        # print(listresult)
        return fastapi.responses.JSONResponse(content={"data":listresult})

        
        


    '''
    def get_data(connection,location_id=None,camera_group_id=None,customer_id=None,subsite_id=None,logger=None):
        """
        Retrives camera configuration data based on the given arguements and joining tcom_Camera_group, tcom_camera_group_list,
        tcom_camera_master, tcom_customer_master,tcom_location_master, tcom_kafka_topics tables.

        Args:
            connection (object): mysql connection object.
            location_id (int) : location_id for filtering
            camera_group_id (int): camera_group_id
            customer_id (int): customer_id
            subsite_id (int): subsite_id

        Returns:
            fastAPI JSONResponse which has camera configuration data.
        """
        if location_id is not None and len(location_id)==1:
                location_id=str(location_id).replace(',','')
        if customer_id is not None and len(customer_id)==1:
                customer_id=str(customer_id).replace(',','')
        if subsite_id is not None and len(subsite_id)==1:
                subsite_id=str(subsite_id).replace(',','')
        if camera_group_id is not None and len(camera_group_id)==1:
                camera_group_id=str(camera_group_id).replace(',','')

        query = ''

        query1=f"select * from tcom_camera_group cg inner join tcom_camera_group_list cl on cg.camera_group_id = cl.camera_group_id inner join tcom_camera_master cm on cl.camera_id = cm.camera_id inner join tcom_kafka_topics kt on kt.camera_id = cm.camera_id inner join tcom_location_master lm on lm.location_id=cm.location_id inner join tcom_customer_master cu on lm.customer_id=cu.customer_id inner join tcom_subsite_master sm on sm.location_id=lm.location_id where lm.location_id in {location_id}"
                
        query2=f"select * from tcom_camera_group cg inner join tcom_camera_group_list cl on cg.camera_group_id = cl.camera_group_id inner join tcom_camera_master cm on cl.camera_id = cm.camera_id inner join tcom_kafka_topics kt on kt.camera_id = cm.camera_id inner join tcom_location_master lm on lm.location_id=cm.location_id inner join tcom_customer_master cu on lm.customer_id=cu.customer_id inner join tcom_subsite_master sm on sm.location_id=lm.location_id where lm.location_id in {location_id} and cu.customer_id in {customer_id}"

        query3=f"select * from tcom_camera_group cg inner join tcom_camera_group_list cl on cg.camera_group_id = cl.camera_group_id inner join tcom_camera_master cm on cl.camera_id = cm.camera_id inner join tcom_kafka_topics kt on kt.camera_id = cm.camera_id inner join tcom_location_master lm on lm.location_id=cm.location_id inner join tcom_customer_master cu on lm.customer_id=cu.customer_id inner join tcom_subsite_master sm on sm.location_id=lm.location_id where lm.location_id in {location_id} and cg.camera_group_id in{camera_group_id}"

        query4=f"select * from tcom_camera_group cg inner join tcom_camera_group_list cl on cg.camera_group_id = cl.camera_group_id inner join tcom_camera_master cm on cl.camera_id = cm.camera_id inner join tcom_kafka_topics kt on kt.camera_id = cm.camera_id inner join tcom_location_master lm on lm.location_id=cm.location_id inner join tcom_customer_master cu on lm.customer_id=cu.customer_id inner join tcom_subsite_master sm on sm.location_id=lm.location_id where lm.location_id in {location_id} and cg.camera_group_id in {camera_group_id} and sm.subsite_id in {subsite_id}"

        query5=f"select * from tcom_camera_group cg inner join tcom_camera_group_list cl on cg.camera_group_id = cl.camera_group_id inner join tcom_camera_master cm on cl.camera_id = cm.camera_id inner join tcom_kafka_topics kt on kt.camera_id = cm.camera_id inner join tcom_location_master lm on lm.location_id=cm.location_id inner join tcom_customer_master cu on lm.customer_id=cu.customer_id inner join tcom_subsite_master sm on sm.location_id=lm.location_id where  cg.camera_group_id in {camera_group_id} "

        
        if location_id and not customer_id and not camera_group_id and not subsite_id:
                query = query1
        elif location_id and customer_id and not camera_group_id and not subsite_id:
                query =query2
        elif location_id and camera_group_id and not subsite_id:
                query=query3
        elif location_id and camera_group_id and subsite_id:
                query=query4
        elif camera_group_id and not location_id and not customer_id and not subsite_id:
                query=query5
         
       
    
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
                    dictdata["camera_group_id"]=i[column_names.index('camera_group_id')] 
                    dictdata["camera_group_name"]=i[column_names.index('camera_group_name')]
                    dictdata["group_description"]=i[column_names.index('group_description')]
                    dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                    dictdata["location_id"]=i[column_names.index('location_id')]
                    dictdata["camera_grouplist_id"]=i[column_names.index('camera_grouplist_id')]
                    dictdata["camera_id"]=i[column_names.index('camera_id')]
                    dictdata["camera_name"]=i[column_names.index('camera_name')]
                    dictdata["fps"]=i[column_names.index('fps')]
                    dictdata["image_height"]=i[column_names.index('image_height')]
                    dictdata["image_width"]=i[column_names.index('image_width')]
                    dictdata["ip"]=i[column_names.index('ip')]
                    dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                    dictdata["password"]=i[column_names.index('password')]
                    dictdata["rtsp_url"]=i[column_names.index('rtsp_url')]
                    dictdata["subsite_id"]=i[column_names.index('subsite_id')]
                    dictdata["user"]=i[column_names.index('user')]
                    dictdata["city"]=i[column_names.index('city')]
                    dictdata["site"]=i[column_names.index('site')]
                    dictdata["time_zone"]=i[column_names.index('time_zone')]
                    dictdata["customer_id"]=i[column_names.index('customer_id')]
                    dictdata["customer_name"]=i[column_names.index('customer_name')]
                    dictdata["sub_site"]=i[column_names.index('sub_site')]
                    dictdata["subsite_id"]=i[column_names.index('subsite_id')]
                    dictdata["subsite_name"]=i[column_names.index('subsite_name')]
                    dictdata["topic_id"]=i[column_names.index('topic_id')]
                    dictdata["partition_id"]=i[column_names.index('partition_id')]
                    dictdata["processing_stage"]=i[column_names.index('processing_stage')]
                    dictdata["tcom_kafka_topicscol"]=i[column_names.index('tcom_kafka_topicscol')]
                    dictdata["topic_name"]=i[column_names.index('topic_name')]
                    dictdata["kafka_id"]=i[column_names.index('kafka_id')]
                    dictdata["location_name"]=i[column_names.index('location_name')]
                    
                    listresult.append(dictdata)

        # print(listresult)
        return fastapi.responses.JSONResponse(content={"data":listresult})


    '''