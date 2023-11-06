import fastapi
class GetScheduleMaster():
    def get_data(connection,camera_group_id=None,logger=None):
        """
        Retrieves scheduling master data from the 'tcom_scheduling_master' table based on provided parameters.

        Args:
            connection (object): MySQL connection object.
            location_id (int): location id for filtering the scheduling data.
            camera_group_id (int): camera_group_id for filtering the scheduling data.
        Returns:
            json dict of scheduling master data
        """
        
        
        if camera_group_id is not None and len(camera_group_id)==1:
                camera_group_id=str(camera_group_id).replace(',','')
        print("=====group id====")
        print(camera_group_id)

        query=""
        if camera_group_id:
            query=f"""select sm.id as schedule_id, sm.timezone_offset, sm.is_deleted ,sm.name as schedule_name, sm.start_date,sm.end_date,sm.status, sm.timezone,sm.timezone_offset,sm.camera_group_id,
                    sm.daily_schedule_id, sm.frequency_type_id,sm.input_type_id,sm.monthly_schedule_id,
                    sm.online_id, sm.preprocess_id, sm.postprocess_id, sm.upload_id, sm.usecase_id, sm.weekly_schedule_id,
                    ft.name as frequency_name from schedule_master sm 
                    inner join frequency_type ft on sm.frequency_type_id=ft.id
                    where  sm.camera_group_id in {camera_group_id} and sm.status=1 """

        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            print(len(resultset))
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    dictdata["schedule_id"]=i[column_names.index('schedule_id')] 
                    dictdata["schedule_name"]=i[column_names.index('schedule_name')]
                    dictdata["camera_group_id"]=i[column_names.index('camera_group_id')]
                    #dictdata["location_id"]=i[column_names.index('location_id')]
                    dictdata["frequency_type_id"]=i[column_names.index('frequency_type_id')]
                    dictdata["status"]=i[column_names.index('status')] 
                    dictdata["preprocess_id"]=i[column_names.index('preprocess_id')]
                    dictdata["postprocess_id"]=i[column_names.index('postprocess_id')]
                    dictdata["usecase_id"]=i[column_names.index('usecase_id')]
                    dictdata["timezone_offset"]=i[column_names.index('timezone_offset')]
                    dictdata["frequency_name"]=i[column_names.index('frequency_name')]
                    dictdata["startdate"]=str(i[column_names.index('start_date')])
                    dictdata["enddate"]=str(i[column_names.index('end_date')])
                    dictdata["monthly_schedule_id"]=i[column_names.index('monthly_schedule_id')]
                    dictdata["weekly_schedule_id"]=i[column_names.index('weekly_schedule_id')]
                    dictdata["daily_schedule_id"]=i[column_names.index('daily_schedule_id')]
                    #dictdata["time_o"]=i[column_names.index('enddate')]
                    
                    # listresult.append(dictdata)
                    if dictdata["frequency_name"].lower()=="monthly":
                        onetime_list = GetScheduleDetails.get_monthly_data(connection,dictdata["monthly_schedule_id"],dictdata["startdate"],dictdata["enddate"])
                        dictdata["monthly_schedule"]=onetime_list
                        print("onetime list====",onetime_list)
                        # for onetime in onetime_list:
                        #     dictdata.update(onetime)

                    if dictdata["frequency_name"].lower()=="daily":
                        daily_list = GetScheduleDetails.get_daily_data(connection,dictdata["daily_schedule_id"],dictdata["startdate"],dictdata["enddate"])
                        dictdata["daily_schedule"]=daily_list
                            # dictdata.update(daily_list[0])

                    if dictdata["frequency_name"].lower()=="weekly":
                        weekly_list = GetScheduleDetails.get_weekly_data(connection,dictdata["weekly_schedule_id"],dictdata["startdate"],dictdata["enddate"])
                        dictdata["weekly_schedule"]=weekly_list
                        
                        # dictdata.update(weekly_list[0])

                    if dictdata["frequency_name"].lower()=="one time":
                        monthly_list = GetScheduleDetails.get_daily_data(connection,dictdata["daily_schedule_id"],dictdata["startdate"],dictdata["enddate"])
                        dictdata["onetime_schedule"]=monthly_list
                        
                    if dictdata["frequency_name"].lower()=="recurring daily":
                        monthly_list = GetScheduleDetails.get_daily_data(connection,dictdata["daily_schedule_id"],dictdata["startdate"],dictdata["enddate"])
                        #dictdata["daily_time"]=monthly_list
                        dictdata["recurring_schedule"]=monthly_list
                        # for eachmonth in monthly_list:
                        #     dictdata.update(eachmonth)
                        # dictdata.update(monthly_list[0])
                    
                    listresult.append(dictdata)

        print(listresult)
        return fastapi.responses.JSONResponse(content={"data":listresult})

class GetScheduleDetails():
    """       
    def get_onetime_data(connection,scheduling_id,logger=None):
                Retrieves one-time scheduling data from the 'tcom_onetime_scheduling' table based on the provided 'scheduling_id'.

        Args:
            connection (object): MySQL connection object.
            scheduling_id (int): scheduling_id for filtering one-time scheduling data.

        Returns:
            json dict of one time scheduling data for given scheduling_id
        
        query=f"select * from tcom_onetime_scheduling where scheduling_id = {scheduling_id}"
    
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            print(len(resultset))
            if len(resultset)>0:
                for i in resultset:
                    print(i)
                    dictdata={}
                    # dictdata["onetime_id"]=i[column_names.index('scheduling_onetime_id')]
                    dictdata["starttime"]=str(i[column_names.index('startdate')])
                    dictdata["endtime"]=str(i[column_names.index('enddate')])
                    dictdata["recurring"]=False
                    dictdata["weekday"]=None
                    dictdata["dayofmonth"]=0

                    listresult.append(dictdata)

        print("listresult===",listresult)
        return listresult
    """
    def get_daily_data(connection,scheduling_id,start_date,end_date,logger=None):
        """
        Retrieves daily scheduling data from the 'tcom_daily_schedule' table based on the provided 'scheduling_id'.

        Args:
            connection (object): MySQL connection object.
            scheduling_id (int): scheduling_id for filtering daily scheduling data.

        Returns:
            json dict of daily scheduling data for given scheduling_id
        """
        if scheduling_id is None:
            return {}
       
        query=f"""select * from daily_schedule ds 
                inner join intervals it on it.daily_schedule_id=ds.id where ds.id = {scheduling_id}"""
    
        print(query)
        listresult=[]
        dictdata={}
        with connection.cursor() as cur:
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            print(len(resultset))

            if len(resultset)>0:
                
                for i in resultset:
                    print(i)
                    
                    if "starttime" not in list(dictdata.keys()):
                        dictdata["starttime"]=[start_date+" "+str(i[column_names.index('start_time')])]
                    else:
                        dictdata["starttime"].append(start_date+" "+str(i[column_names.index('start_time')]))
                    
                    if "endtime" not in list(dictdata.keys()):
                        dictdata["endtime"]=[end_date+" "+str(i[column_names.index('end_time')])]
                    else:
                        dictdata["endtime"].append(end_date+" "+str(i[column_names.index('end_time')]))

                    # if "weekday" not in list(dictdata.keys()):
                    #     dictdata["weekday"] = [i[column_names.index('name')]]
                    # else:
                    #     dictdata["weekday"].append(i[column_names.index('name')])
        print(dictdata)
        return dictdata
    
    def get_weekly_data(connection,scheduling_id,start_date,end_date,logger=None):
        """
        Retrieves weekly scheduling data from the 'tcom_weekly_schedule' table based on the provided 'scheduling_id'.

        Args:
            connection (object): MySQL connection object.
            scheduling_id (int): scheduling_id for filtering weekly scheduling data.

        Returns:
            json dict of weekly scheduling data for given scheduling_id
        """
        if scheduling_id is None:
            return {}
        query=f"""SELECT * FROM weekly_schedule ws
                    inner join weeklyschedule_weekdays_link wwl on ws.id=wwl.weekly_schedule_id
                    inner join week_days wd on wwl.weekday_id= wd.id  where  ws.id = {scheduling_id}"""
    
        print(query)
        listresult=[]
        dictdata={}
        with connection.cursor() as cur:
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            print(len(resultset))
            if len(resultset)>0:
                
                for i in resultset:
                    print(i)
                    
                    if "starttime" not in list(dictdata.keys()):
                        dictdata["starttime"]=[start_date+" "+str(i[column_names.index('start_time')])]
                    else:
                        dictdata["starttime"].append(start_date+" "+str(i[column_names.index('start_time')]))
                    
                    if "endtime" not in list(dictdata.keys()):
                        dictdata["endtime"]=[end_date+" "+str(i[column_names.index('end_time')])]
                    else:
                        dictdata["endtime"].append(end_date+" "+str(i[column_names.index('end_time')]))

                    if "weekday" not in list(dictdata.keys()):
                        dictdata["weekday"] = [i[column_names.index('name')]]
                    else:
                        dictdata["weekday"].append(i[column_names.index('name')])

                    
                    

                    #listresult.append(dictdata)

        print(dictdata)
        return dictdata


    def get_monthly_data(connection,schedule_id,start_date,end_date,logger=None):
        """
        Retrieves monthly scheduling data from the 'tcom_monthly_schedule' table based on the provided 'scheduling_id'.

        Args:
            connection (object): MySQL connection object.
            scheduling_id (int): scheduling_id for filtering monthly scheduling data.

        Returns:
            json dict of monthly scheduling data for given scheduling_id
        """
        if schedule_id is None:
            return {}
        query=f"""SELECT md.date, ms.start_time, ms.end_time FROM monthly_days md  inner join 
monthly_schedule ms on  md.monthly_schedule_id=ms.id where ms.id ={schedule_id}"""
    
        print(query)
        listresult=[]
        dictdata={}
        with connection.cursor() as cur:
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            print(len(resultset))
            if len(resultset)>0:
                
                for i in resultset:
                    print(i)
                    
                    if "starttime" not in list(dictdata.keys()):
                        dictdata["starttime"]=[start_date+" "+str(i[column_names.index('start_time')])]
                    else:
                        dictdata["starttime"].append(start_date+" "+str(i[column_names.index('start_time')]))
                    
                    if "endtime" not in list(dictdata.keys()):
                        dictdata["endtime"]=[end_date+" "+str(i[column_names.index('end_time')])]
                    else:
                        dictdata["endtime"].append(end_date+" "+str(i[column_names.index('end_time')]))

                    if "date" not in list(dictdata.keys()):
                        dictdata["date"] = [""]
                    else:
                        dictdata["date"].append(i[column_names.index('date')])


        print(dictdata)
        return dictdata