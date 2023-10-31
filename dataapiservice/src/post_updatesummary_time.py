class UpdateIncidentSummaryTime():
    def update(cnx,starttime,endtime):
        print("========in update summary time=============")
        query="""insert into incident_summary_time (start_time, end_time) VALUES (%s, %s)"""
        try:
            with cnx.cursor() as cur:
                print("Inserting")
                print(query, starttime,endtime)
                cur.execute(query, (starttime,endtime,))
                cnx.commit()
            return {"data":"Updated incident_summary_time"}
        except Exception as ex:
            print("======",ex)
            return {"data":ex}