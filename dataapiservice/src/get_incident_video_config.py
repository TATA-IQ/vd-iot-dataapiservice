class GetIncidentVideoData():
    def get_data(connection,incident_video_id):
        query=f"""SELECT iv.id as incident_video_id, iv.status,iv.file_name, iv.incident_id,iv.camera_id,iv.usecase_id,iv.start_timestamp,iv.end_timestamp,cm.zone_id,cm.timezone,sm.subsite_id,lm.location_id,lm.customer_id,lm.city_id,iv.is_deleted,cm.camera_status,cm.fps,cm.image_height,cm.image_width,cm.rtsp_url
                    FROM incident_video iv
                    INNER JOIN camera_master cm ON iv.camera_id = cm.camera_id
                    INNER JOIN zone_master zm ON cm.zone_id = zm.zone_id
                    INNER JOIN subsite_master sm ON zm.subsite_id = sm.subsite_id
                    INNER JOIN location_master lm ON sm.location_id = lm.location_id
                    where iv.id={incident_video_id} 
        """
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query)
            column_names = [i[0] for i in cur.description]

            for i in cur:
                dictdata={}
                dictdata["incident_video_id"]=i[column_names.index('incident_video_id')] 
                dictdata["camera_id"]=i[column_names.index('camera_id')]
                dictdata["start_timestamp"]=i[column_names.index('start_timestamp')]
                dictdata["end_timestamp"]=i[column_names.index('end_timestamp')]
                dictdata["is_deleted"]=i[column_names.index('is_deleted')]
                dictdata["file_name"]=i[column_names.index('file_name')]
                dictdata["incident_id"]=i[column_names.index('incident_id')]
                dictdata["image_height"]=i[column_names.index('image_height')]
                dictdata["image_width"]=i[column_names.index('image_width')]
                dictdata["rtsp_url"]=i[column_names.index('rtsp_url')]
                # dictdata["user"]=i[column_names.index('user')]
                try:
                    dictdata["time_zone"]=i[column_names.index('time_zone')]
                except:
                    dictdata["time_zone"]=""
                dictdata["customer_id"]=i[column_names.index('customer_id')]
                dictdata["location_id"]=i[column_names.index('location_id')]
                dictdata["subsite_id"]=i[column_names.index('subsite_id')]
                # dictdata["site_id"]=i[column_names.index('site_id')]
                dictdata["zone_id"]=i[column_names.index('zone_id')]
                dictdata["city_id"]=i[column_names.index('city_id')]
                dictdata["usecase_id"]=i[column_names.index('usecase_id')]
                # dictdata["incident_summary_id"]=i[column_names.index('incident_summary_id')]
                listresult.append(dictdata)
                print(dictdata)
                
        return {"data":listresult} 
    


class UpdateIncidentVideoStatus():
    def update(cnx,incident_video_id,status,message):
        query="""update incident_video set status=%s, message=%s where id=%s"""
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                print(query)
                cur.execute(query,(status,message,incident_video_id))
                cnx.commit()
                # cnx.close()
                print(f"status: {status} and {message} for incident_video_id: {incident_video_id}")
            return {"data":"Updated status for incident_video"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}
        # finally:
        #     cnx.close()     
            
            
            




        


    
