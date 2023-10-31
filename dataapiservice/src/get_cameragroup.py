# import sqlalchemy
import fastapi
import pandas as pd
class GetModelCamGroup():
    def get_data(connection,location_id=None,customer_id=None,subsite_id=None,zone_id=None,logger=None):
        """
        Retrives camera group data based on the given arguements and joining tcom_Camera_group, 
        tcom_subsite_master, tcom_location_mastertables.

        Args:
            connection (object): mysql connection object.
            location_id (int) : location_id for filtering
            customer_id (int): customer_id
            subsite_id (int): subsite_id

        Returns:
            fastAPI JSONResponse which has camera group data.
        """

        print("data==>",location_id,customer_id)
        if location_id is not None and len(location_id)==1:
                location_id=str(location_id).replace(',','')
        if customer_id is not None and len(customer_id)==1:
                customer_id=str(customer_id).replace(',','')
        if subsite_id is not None and len(subsite_id)==1:
                subsite_id=str(subsite_id).replace(',','')
        if zone_id is not None and len(zone_id)==1:
                zone_id=str(zone_id).replace(',','')
        query = ''

        query1=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                inner join zone_master zm on zm.subsite_id = sm.subsite_id
                where sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 
                and zm.is_deleted=0 and cg.location_id in {location_id}"""
        query2=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                inner join zone_master zm on zm.subsite_id = sm.subsite_id
                where sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 
                and zm.is_deleted=0 and zm.zone_id in {zone_id}"""
                
        query3=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on  cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                where sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 and sm.subsite_id in {subsite_id}"""

        query4=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on  cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                where  sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 and  lm.customer_id  in {customer_id}"""
        query5=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on  cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                where  sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 
                and  lm.customer_id in {customer_id} and lm.location_id in {location_id}"""
        
        query6=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on  cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                inner join zone_master zm on zm.subsite_id = sm.subsite_id
                where  sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 and zm.is_deleted=0
                and zm.zone_id in {zone_id} lm.customer_id in {customer_id} and lm.location_id in {location_id} and sm.subsite_id in {subsite_id} and zm.zone_id in {zone_id}"""
        
        
        query7=f"""SELECT cg.camera_group_id from camera_group cg 
                inner join location_master lm on  cg.location_id=lm.location_id 
                inner join subsite_master sm on cg.location_id=sm.location_id 
                inner join zone_master zm on zm.subsite_id = sm.subsite_id
                where  sm.is_deleted=0 and lm.is_deleted=0 and cg.is_deleted=0 and zm.is_deleted=0"""
        
        if location_id and customer_id and subsite_id:
            query = query6
        elif location_id and customer_id and not subsite_id:
            query =query5
        elif  subsite_id:
            query=query3
        elif location_id :
            query=query1
        elif  customer_id :
            query=query4
        elif zone_id:
            query=query2
        else:
            query=query7
         
       
    
        print(query)
        listresult=[]
        with connection.cursor() as cur:
            cur.execute(query)
            if cur.description is None:
                print("query===",query)
                return  fastapi.responses.JSONResponse(content={"data":{query},"error":"Please check params"})
           
            column_names = [i[0] for i in cur.description]
            resultset=cur.fetchall()
            #print(len(resultset))
            if len(resultset)>0:
                for i in resultset:
                    #print(i)
                    dictdata={}
                    #dictdata["camera_group_id"]=
                    listresult.append(i[column_names.index('camera_group_id')])
            return fastapi.responses.JSONResponse(content={"data":list(set(listresult))})
            
    