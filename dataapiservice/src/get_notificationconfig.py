class GetNotificationDetails():
    def get_eventbased_notification_data(connection,camera_id, usecase_id ,logger=None):
        """ 
        Retrives event based notification data by filtering the camera id and usecase id
        Args:
            connection (object): mysql connection object
            camera_id (int): camera_id for which camera data is needed
            usecase_id (int): usecase_id for which usecase data is needed
        Returns:
            Event based notification details
        """
        
        query="""select np.id notification_id, np.frequency_id, np.name notification_name, np.location_id, np.shift_timing_id, camlist.nplevel, camlist.camera_id, uc.usecase_id, uc.incident_id from notification np
                inner join
                (select notification_id, 'camera' nplevel, camera_master_id camera_id from notification_camera_link
                union all
                select nz.notification_id, 'zone' nplevel, cm.camera_id from notification_zone_link nz inner join camera_master cm on nz.zone_master_id = cm.zone_id
                union all
                select ns.notification_id, 'subsite' nplevel, cm.camera_id from notification_subsite_link ns inner join zone_master zm on ns.subsite_master_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                union all
                select nl.notification_id, 'site' nplevel, cm.camera_id from notification_location_link nl inner join subsite_master sm on nl.location_master_id = sm.location_id inner join zone_master zm on sm.subsite_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                ) camlist on camlist.notification_id = np.id
                inner join notification_usecase_incident_link uc on uc.notification_id = np.id
                where np.frequency_id=3 and np.status=1 
                and camera_id=%s and usecase_id=%s"""
        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (camera_id,usecase_id,))
            column_names = [i[0] for i in cur.description]
            for i in cur:
                dictdata={}
                dictdata["notification_id"]=i[column_names.index('notification_id')] 
                dictdata["frequency_id"]=i[column_names.index('frequency_id')] 
                dictdata["notification_name"]=i[column_names.index('notification_name')] 
                dictdata["location_id"]=i[column_names.index('location_id')] 
                dictdata["nplevel"]=i[column_names.index('nplevel')] 
                dictdata["camera_id"]=i[column_names.index('camera_id')] 
                dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                dictdata["incident_id"]=i[column_names.index('incident_id')]
                
                listresult.append(dictdata)


        return {"data":listresult}
    
    def get_hourly_notification_data(connection,camera_id, usecase_id ,logger=None):
        """ 
        Retrives hourly based notification data by filtering the camera id and usecase id
        Args:
            connection (object): mysql connection object
            camera_id (int): camera_id for which camera data is needed
            usecase_id (int): usecase_id for which usecase data is needed
        Returns:
            hourly based notification details
        """
        
        query="""select np.id notification_id, np.frequency_id, np.name notification_name, np.location_id, np.shift_timing_id, camlist.nplevel, camlist.camera_id, uc.usecase_id, uc.incident_id from notification np
                inner join
                (select notification_id, 'camera' nplevel, camera_master_id camera_id from notification_camera_link
                union all
                select nz.notification_id, 'zone' nplevel, cm.camera_id from notification_zone_link nz inner join camera_master cm on nz.zone_master_id = cm.zone_id
                union all
                select ns.notification_id, 'subsite' nplevel, cm.camera_id from notification_subsite_link ns inner join zone_master zm on ns.subsite_master_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                union all
                select nl.notification_id, 'site' nplevel, cm.camera_id from notification_location_link nl inner join subsite_master sm on nl.location_master_id = sm.location_id inner join zone_master zm on sm.subsite_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                ) camlist on camlist.notification_id = np.id
                inner join notification_usecase_incident_link uc on uc.notification_id = np.id
                where np.frequency_id=1 and np.status=1 and
                camera_id=%s and usecase_id=%s"""
        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (camera_id,usecase_id,))
            column_names = [i[0] for i in cur.description]
            for i in cur:
                dictdata={}
                dictdata["notification_id"]=i[column_names.index('notification_id')] 
                dictdata["frequency_id"]=i[column_names.index('frequency_id')] 
                dictdata["notification_name"]=i[column_names.index('notification_name')] 
                dictdata["location_id"]=i[column_names.index('location_id')] 
                dictdata["nplevel"]=i[column_names.index('nplevel')] 
                dictdata["camera_id"]=i[column_names.index('camera_id')] 
                dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                dictdata["incident_id"]=i[column_names.index('incident_id')]
                
                listresult.append(dictdata)


        return {"data":listresult}
    
    def get_endshiftbased_data(connection,camera_id, usecase_id ,logger=None):
        """ 
        Retrives End of the shift based notification data by filtering the camera id and usecase id
        Args:
            connection (object): mysql connection object
            camera_id (int): camera_id for which camera data is needed
            usecase_id (int): usecase_id for which usecase data is needed
        Returns:
            End of the shift based notification details
        """
        
        query="""select np.id notification_id, np.frequency_id, np.name notification_name, np.location_id, np.shift_timing_id, camlist.nplevel, camlist.camera_id, uc.usecase_id, uc.incident_id,
                tm.start_time, tm.end_time, st.time_zone from notification np
                inner join
                (select notification_id, 'camera' nplevel, camera_master_id camera_id from notification_camera_link
                union all
                select nz.notification_id, 'zone' nplevel, cm.camera_id from notification_zone_link nz inner join camera_master cm on nz.zone_master_id = cm.zone_id
                union all
                select ns.notification_id, 'subsite' nplevel, cm.camera_id from notification_subsite_link ns inner join zone_master zm on ns.subsite_master_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                union all
                select nl.notification_id, 'site' nplevel, cm.camera_id from notification_location_link nl inner join subsite_master sm on nl.location_master_id = sm.location_id inner join zone_master zm on sm.subsite_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                ) camlist on camlist.notification_id = np.id
                inner join shift_timings st on st.id = np.shift_timing_id
                inner join timings tm on st.id = tm.shift_timing_id
                inner join notification_usecase_incident_link uc on uc.notification_id = np.id
                where np.frequency_id=2 and np.status=1
                and camera_id=%s and usecase_id=%s"""
        
        listresult=[]
        with connection.cursor() as cur:
            res=[]
            cur.execute(query, (camera_id,usecase_id,))
            column_names = [i[0] for i in cur.description]
            for i in cur:
                dictdata={}
                dictdata["notification_id"]=i[column_names.index('notification_id')] 
                dictdata["frequency_id"]=i[column_names.index('frequency_id')] 
                dictdata["notification_name"]=i[column_names.index('notification_name')] 
                dictdata["location_id"]=i[column_names.index('location_id')] 
                dictdata["shift_timing_id"]=i[column_names.index('shift_timing_id')] 
                dictdata["nplevel"]=i[column_names.index('nplevel')] 
                dictdata["camera_id"]=i[column_names.index('camera_id')] 
                dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                dictdata["incident_id"]=i[column_names.index('incident_id')]
                dictdata["start_time"]=i[column_names.index('start_time')]
                dictdata["end_time"]=i[column_names.index('end_time')]
                dictdata["time_zone"]=i[column_names.index('time_zone')]
                
                listresult.append(dictdata)


        return {"data":listresult}
    
    def get_notification_data_bycameraid(connection,camera_id, logger=None):
        """ 
        Retrives End of the shift based notification data by filtering the camera id and usecase id
        Args:
            connection (object): mysql connection object
            camera_id (int): camera_id for which camera data is needed
        Returns:
            End of the shift based notification details
        """
        if camera_id is None:
            query="""select np.id notification_id, np.frequency_id, np.name notification_name, np.location_id, np.shift_timing_id, camlist.nplevel, camlist.camera_id, uc.usecase_id, uc.incident_id, tm.start_time, tm.end_time, st.time_zone from notification np
            inner join
            (select notification_id, 'camera' nplevel, camera_master_id camera_id from notification_camera_link
            union all
            select nz.notification_id, 'zone' nplevel, cm.camera_id from notification_zone_link nz inner join camera_master cm on nz.zone_master_id = cm.zone_id
            union all
            select ns.notification_id, 'subsite' nplevel, cm.camera_id from notification_subsite_link ns inner join zone_master zm on ns.subsite_master_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
            union all
            select nl.notification_id, 'site' nplevel, cm.camera_id from notification_location_link nl inner join subsite_master sm on nl.location_master_id = sm.location_id inner join zone_master zm on sm.subsite_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
            ) camlist on camlist.notification_id = np.id
            inner join notification_usecase_incident_link uc on uc.notification_id = np.id
            left join shift_timings st on st.id = np.shift_timing_id
            left join timings tm on st.id = tm.shift_timing_id
            """
            listresult=[]
            with connection.cursor() as cur:
                res=[]
                cur.execute(query)
                column_names = [i[0] for i in cur.description]
                for i in cur:
                    dictdata={}
                    dictdata["notification_id"]=i[column_names.index('notification_id')] 
                    dictdata["frequency_id"]=i[column_names.index('frequency_id')] 
                    dictdata["notification_name"]=i[column_names.index('notification_name')] 
                    dictdata["location_id"]=i[column_names.index('location_id')] 
                    dictdata["shift_timing_id"]=i[column_names.index('shift_timing_id')] 
                    dictdata["nplevel"]=i[column_names.index('nplevel')] 
                    dictdata["camera_id"]=i[column_names.index('camera_id')] 
                    dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                    dictdata["incident_id"]=i[column_names.index('incident_id')]
                    dictdata["start_time"]=i[column_names.index('start_time')]
                    dictdata["end_time"]=i[column_names.index('end_time')]
                    dictdata["time_zone"]=i[column_names.index('time_zone')]
                    
                    listresult.append(dictdata)
            
            # resultdict={}
            # for i in listresult:
            #     camera_id = i["camera_id"]
            #     usecase_id = i["usecase_id"]
            #     if camera_id not in resultdict:
            #         resultdict[camera_id]={}
            #     if usecase_id not in resultdict[camera_id]:
            #         resultdict[camera_id][usecase_id]=[]
            #     a={}
            #     for k,v in i.items():
            #         a[k]=v
                    
            #     resultdict[camera_id][usecase_id].append(a)
                    
            # print("resultdict=====", resultdict)
            print("listresult=====", listresult)
            # import pandas as pd
            # df = pd.DataFrame(listresult)
            # df.to_csv("df.csv")

            return {"data":listresult}
        else:
            query="""select np.id notification_id, np.frequency_id, np.name notification_name, np.location_id, np.shift_timing_id, camlist.nplevel, camlist.camera_id, uc.usecase_id, uc.incident_id, tm.start_time, tm.end_time, st.time_zone  from notification np
                inner join
                (select notification_id, 'camera' nplevel, camera_master_id camera_id from notification_camera_link
                union all
                select nz.notification_id, 'zone' nplevel, cm.camera_id from notification_zone_link nz inner join camera_master cm on nz.zone_master_id = cm.zone_id
                union all
                select ns.notification_id, 'subsite' nplevel, cm.camera_id from notification_subsite_link ns inner join zone_master zm on ns.subsite_master_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                union all
                select nl.notification_id, 'site' nplevel, cm.camera_id from notification_location_link nl inner join subsite_master sm on nl.location_master_id = sm.location_id inner join zone_master zm on sm.subsite_id = zm.subsite_id inner join camera_master cm on zm.zone_id = cm.zone_id
                ) camlist on camlist.notification_id = np.id
                inner join notification_usecase_incident_link uc on uc.notification_id = np.id
                left join shift_timings st on st.id = np.shift_timing_id
                left join timings tm on st.id = tm.shift_timing_id
                where camera_id=%s"""
        
            listresult=[]
            with connection.cursor() as cur:
                res=[]
                cur.execute(query, (camera_id,))
                column_names = [i[0] for i in cur.description]
                for i in cur:
                    dictdata={}
                    dictdata["notification_id"]=i[column_names.index('notification_id')] 
                    dictdata["frequency_id"]=i[column_names.index('frequency_id')] 
                    dictdata["notification_name"]=i[column_names.index('notification_name')] 
                    dictdata["location_id"]=i[column_names.index('location_id')] 
                    dictdata["shift_timing_id"]=i[column_names.index('shift_timing_id')] 
                    dictdata["nplevel"]=i[column_names.index('nplevel')] 
                    dictdata["camera_id"]=i[column_names.index('camera_id')] 
                    dictdata["usecase_id"]=i[column_names.index('usecase_id')] 
                    dictdata["incident_id"]=i[column_names.index('incident_id')]
                    dictdata["start_time"]=i[column_names.index('start_time')]
                    dictdata["end_time"]=i[column_names.index('end_time')]
                    dictdata["time_zone"]=i[column_names.index('time_zone')]
                    
                    listresult.append(dictdata)
            
            resultdict={}
            for i in listresult:
                camera_id = i["camera_id"]
                usecase_id = i["usecase_id"]
                if camera_id not in resultdict:
                    resultdict[camera_id]={}
                if usecase_id not in resultdict[camera_id]:
                    resultdict[camera_id][usecase_id]=[]
                a={}
                for k,v in i.items():
                    a[k]=v
                    
                resultdict[camera_id][usecase_id].append(a)
                    
            print("resultdict=====", resultdict)
            print("listresult=====", listresult)

            return {"data":listresult}
