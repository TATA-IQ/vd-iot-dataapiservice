class GetSummaryTimeDetails():
    def get_data(connection):
        """ 
        Retrives latest summary start time and endtime data by filtering the incident_summary_time table 
        Args:
            connection (object): mysql connection object
        Returns:
           start time and endtime of incident_summary_time
        """
        
        query="""select * from incident_summary_time ORDER BY id DESC LIMIT 1"""
        # query="""select * from incident_summary_time"""
        
        listresult=[]
        with connection.cursor(buffered=True) as cur: 
            cur.execute(query)
            column_names = [i[0] for i in cur.description]
            if cur.rowcount == 0:
                listresult.append({"id": None, "start_time": None, "end_time": None})
            else:
                for i in cur:
                    dictdata={}
                    dictdata["id"]=i[column_names.index('id')] 
                    dictdata["start_time"]=i[column_names.index('start_time')] 
                    dictdata["end_time"]=i[column_names.index('end_time')] 

                    listresult.append(dictdata)

        # return {"data":listresult}
        return {"data":listresult}
