from fastapi import FastAPI
from config_parser.parser import Config
import logging
from logging.handlers import TimedRotatingFileHandler
from model.camera_config_model import CameraDetails, CameraConfig
from model.camera_group_model import CameraGroup,CameraIDs
from model.model_config_model import ModelConfig
from model.model_master_model import ModelMasterEndpoint, ModelMaster
from model.preprocess_model import PreprocessConfig,PreprocessConfigByid
from model.schedule_model import ScheduleMaster
from model.usecase_model import UseCaseModel
from model.model_validate_model import ModelValidation
from model.post_process_model import PostProcessConf, PostProcessClass, PostProcessIncident, PostProcessComputation, PostProcessBoundary
from model.incidentvideo_model import IncidentVideo, UpdateIncidentVideo
from model.notification_model import notification_config,camera_config
from src.get_cameragroup import GetModelCamGroup
from src.get_cameraconfig import GetCameraConfigData
from src.get_preprocessconfig import GetPreProcessConfigData
from src.get_schedulingconfig import GetScheduleMaster
from src.get_online import GetOnline
from src.get_upload import GetUpload
from src.get_cameraextract import GetCameraFrames
from src.get_modelmaster import GetModelMasterById
from src.post_updatemodelurl import UpdateEndPoint, UpdateModelStatus
from src.get_boundary import GetBoundaryData
from src.get_classes import GetClassesData
from src.get_computation import GetComputationData
from src.get_cameraid import GetModelCamId
from src.get_incidents import GetIncidentData
from src.get_postprocess import GetPostProcessConfigData
from src.get_usecase import GetUsecase
from src.get_kafkatopics import GetKafkaData
from src.get_kafkatopics_bycamid import GetKafkaDataByCamid
from src.get_incident_video_config import GetIncidentVideoData, UpdateIncidentVideoStatus
from src.get_model_validation import ValidationModel
from model.kafka_model import KafkaTopics,KafkaTopicsCamId
from model.model_port_model import ModelPorts, ModelStatus
from src.get_port_details import GetPortDetails
from src.post_updateportmodel import UpdateModelPort
from src.get_incident_summary_details import GetSummaryTimeDetails
from src.post_updatesummary_time import UpdateIncidentSummaryTime
from src.get_notificationconfig import GetNotificationDetails
from src.get_preprocessconfig_byid import GetPreProcessConfigDataById
from model.incident_summary_time import SummaryTime
import time

import mysql.connector
import socket
import consul
# from src.parser import Config
import socket

config = Config.yamlconfig("config/config.yaml")[0]
dbconfig=config["db"]
# validateconfig=config["validation_api"]
local_ip=socket.gethostbyname(socket.gethostname())
consul_conf=config["consul"]
service_conf=config["register_service"]

print(dbconfig)

def connection_sql():
        try:
                cnx = mysql.connector.connect(
                user=dbconfig["username"],
                password=dbconfig["password"],
                host=dbconfig["host"],
                database=dbconfig["db"],
                port=dbconfig["port"]
                )
                return cnx
        except Exception as exp:
                print("expection raised", exp)
                cnx = mysql.connector.connect(
                user=dbconfig["username"],
                password=dbconfig["password"],
                host=dbconfig["host"],
                database=dbconfig["db"],
                )
                return cnx
                

cnx=connection_sql()

# cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mysqlpool", pool_size=5,
#                                                       user=dbconfig["username"],
#                                                       password=dbconfig["password"],
#                                                       host=dbconfig["host"],
#                                                       database=dbconfig["db"])

def check_service_address(consul_client,service_name,env):
    
        
    try:
        services=consul_client.catalog.service(service_name)[1]
        console.info(f" Service Extracted from Cosnul For {service_name} : {services}")
        for i in services:
            if env == i["ServiceID"].split("-")[-1]:
                return i["ServiceID"]
    except:
        time.sleep(10)
        pass
    return None

def get_local_ip():
        '''
        Get the ip of server
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(("192.255.255.255", 1))
            IP = s.getsockname()[0]
        except:
            IP = "127.0.0.1"
        finally:
            s.close()
        return IP
def register_service(consul_conf):
    consul_client = consul.Consul(host=consul_conf["host"],port=consul_conf["port"])
    name=socket.gethostname()
    servicecheck=check_service_address(consul_client,"dbapi",consul_conf["env"])
    if servicecheck is None:
        consul_client.agent.service.register(
        "dbapi",service_id=name+"-dbapi-"+consul_conf["env"],
        port=service_conf["port"],
        address=get_local_ip(),
        tags=["python","dbapi",consul_conf["env"]]
        )

    else:
        consul_client.agent.service.deregister(servicecheck["ServiceID"])
        consul_client.agent.service.register(
        "dbapi",service_id=name+"-dbapi-"+consul_conf["env"],
        port=service_conf["port"],
        address=get_local_ip(),
        tags=["python","dbapi",consul_conf["env"]]
        )





register_service(consul_conf)
app = FastAPI()


@app.get("/getCameraGroup")
async def model_cameragroup_fetch(data: CameraGroup):
    """
    This endpoint fetches tcom camera group data.

    Args:
            data (object): Tcom_CameraGroup data object with parameters.
            - location_id (int): location id to filter camera groups.
            - customer_id (int): customer id  to filter.
            - subsite_id (int): subsite id to filter.

    Returns:
            FastAPI JSONResponse of camera group data.
    """
    print("-----------cameragroup------------")
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()

    print("=====",data)
    try:
        cnx.cmd_refresh(1)
        return GetModelCamGroup.get_data(
                cnx, data.location_id, data.customer_id, data.subsite_id, data.zone_id
        )
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        return GetModelCamGroup.get_data(
                cnx, data.location_id, data.customer_id, data.subsite_id, data.zone_id
        )

@app.get("/getCameraId")
async def model_cameraid_fetch(data: CameraIDs):
    """
    This endpoint fetches tcom camera group data.

    Args:
            data (object): Tcom_CameraGroup data object with parameters.
            - location_id (int): location id to filter camera groups.
            - customer_id (int): customer id  to filter.
            - subsite_id (int): subsite id to filter.
            - camera_group_id (int): camera_group_id to filter

    Returns:
            FastAPI JSONResponse of camera group data.
    """
    print("-----------cameraid------------")
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()

    print("=====",data)
    try:
        cnx.cmd_refresh(1)
        return GetModelCamId.get_data(
                cnx, data.location_id, data.customer_id, data.subsite_id, data.zone_id, data.camera_group_id
        )
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        return GetModelCamGroup.get_data(
                cnx, data.location_id, data.customer_id, data.subsite_id, data.zone_id
        )

@app.get("/getCameraConfig")
async def camera_config_fetch(data: CameraConfig):
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
    try:
        #     cnx.close()
        cnx.cmd_refresh(1)
        data = GetCameraConfigData.get_data(
                cnx, data.camera_group_id
        )
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data = GetCameraConfigData.get_data(
                cnx, data.camera_group_id
        )
        #     cnx.close()
        return data


@app.post("/updateEndpoint")
async def endpoint_update(data: ModelMasterEndpoint):
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()

    print("update===>", data)
    print("*******", data.model_end_point)
    print("*******", data.model_id)
#     cnx.close()
    try:
        cnx.cmd_refresh(1)
        data= UpdateEndPoint.update(cnx, data.model_end_point, data.model_id)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data= UpdateEndPoint.update(cnx, data.model_end_point, data.model_id)
        return data

@app.get("/getusecase")
async def usecase_fetch():
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
#     cnx.close()

    try:
        cnx.cmd_refresh(1)
        data = GetUsecase.get_data(cnx)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data = GetUsecase.get_data(cnx)
        return data


@app.get("/getModelMasterbyId")
async def model_master_by_id_fetch(data: ModelMaster):
    """
    This endpoint fetches Model Master data for a given model id.
    Args:
    Returns:
            FastAPI JSONResponse of Model Master data.
    """
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
#     cnx.close()
    try:
        cnx.cmd_refresh(1)
        data =GetModelMasterById.get_data(cnx, data.model_id)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data =GetModelMasterById.get_data(cnx, data.model_id)
        return data


# @app.get("/getModelConfigbyId")
# async def ModelConfigById_fetch(data: ModelConfig):
#     """
#     This endpoint fetches Model config data for a given model id.
#     Args:
#     Returns:
#             FastAPI JSONResponse of Model config data.
#     """

#     # # cnx=connection_sql()
#      # #  cnx = cnxpool.get_connection()
#     if data.location_id != None and data.model_id != None:
#         return GetModelConfigById.get_data(cnx, data.model_id, data.location_id)
#     else:
#         return GetModelConfigById.get_data(cnx, data.model_id)


@app.get("/getScheduleMaster")
async def schedule_master_fetch(data: ScheduleMaster):
    """
    This endpoint fetches schedule master data.
    Args:
    Returns:
            FastAPI JSONResponse of schedule master data.
    """
    print("====schedule=====")
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
#     cnx.close()

    try:
        cnx.cmd_refresh(1)
        data= GetScheduleMaster.get_data(cnx, data.camera_group_id)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data= GetScheduleMaster.get_data(cnx, data.camera_group_id)
        return data



@app.get("/getPreprocessConfig")
async def preprocess_config_fetch(data: PreprocessConfig):
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
#     cnx.close()
    try:
        cnx.cmd_refresh(1)
        data= GetPreProcessConfigData.get_data(cnx, data.camera_group_id)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data= GetPreProcessConfigData.get_data(cnx, data.camera_group_id)
        return data
@app.get("/getPreprocessByid")
async def preprocess_config_fetch(data: PreprocessConfigByid):
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
#     cnx.close()
    try:
        cnx.cmd_refresh(1)
        data= GetPreProcessConfigDataById.get_data(cnx, data.preprocess_id)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data= GetPreProcessConfigData.get_data(cnx, data.preprocess_id)
        return data


@app.get("/getModelMasterbyId")
async def model_master_by_id_fetch(data:ModelMaster):
        """
        This endpoint fetches Model Master data for a given model id. 
        Args:
        Returns:
                FastAPI JSONResponse of Model Master data.
        """
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()
        try:
                cnx.cmd_refresh(1)
                return GetModelMasterById.get_data(cnx,data.model_id)
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                return GetModelMasterById.get_data(cnx,data.model_id)


@app.post("/updateEndpoint")
async def endpoint_update(data:ModelMasterEndpoint):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.model_end_point)
        print("*******",data.model_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= UpdateEndPoint.update(cnx,data.model_end_point,data.model_id)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= UpdateEndPoint.update(cnx,data.model_end_point,data.model_id)
                return data


@app.get("/getpostprocess")
async def post_process_config_fetch(data:PostProcessConf):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        #print("*******",data.camera_group_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetPostProcessConfigData.get_data(cnx,data.usecase_id)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetPostProcessConfigData.get_data(cnx,data.usecase_id)
                return data 


@app.get("/getclasses")
async def post_process_class_fetch(data:PostProcessClass):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.usecase_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetClassesData.get_data(cnx,data.usecase_id)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetClassesData.get_data(cnx,data.usecase_id)
                return data


@app.get("/getincidents")
async def post_process_incidents_fetch(data:PostProcessIncident):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.usecase_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetIncidentData.get_data(cnx,data.usecase_id)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetIncidentData.get_data(cnx,data.usecase_id)
                return data
        


@app.get("/getcomputation")
async def post_process_computation_fetch(data:PostProcessComputation):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.usecase_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetComputationData.get_data(cnx,data.usecase_id)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetComputationData.get_data(cnx,data.usecase_id)
                return data

@app.get("/getonline")
async def online_fetch():
        
        print("===hitting online===")
        try:
                cnx.cmd_refresh(1)
                data= GetOnline.get_data(cnx)
                return data
        except Exception as ex:
                print(ex)
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetOnline.get_data(cnx)
                return data

@app.get("/getupload")
async def upload_fetch():
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        # print("update===>",data)
        # print("*******",data.usecase_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetUpload.get_data(cnx)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetUpload.get_data(cnx)
                return data

@app.get("/getboundary")
async def post_process_boundary_fetch(data:PostProcessBoundary):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.usecase_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetBoundaryData.get_data(cnx,data.usecase_id)
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data= GetBoundaryData.get_data(cnx,data.usecase_id)
                return data

@app.get("/gettopics")
async def kafka_topics_fetch(data:KafkaTopics):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.camera_group_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetKafkaData.get_data(cnx,data.camera_group_id)
                return data
        except:
                cnx.reconnect()
                data= GetKafkaData.get_data(cnx,data.camera_group_id)
                cnx.cmd_refresh(1)
                return data
@app.get("/gettopicsbycamid")
async def kafka_topicsbycamid_fetch(data:KafkaTopicsCamId):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()

        print("update===>",data)
        print("*******",data.camera_id)
        
        # cnx.close()
        try:
                cnx.cmd_refresh(1)
                data= GetKafkaDataByCamid.get_data(cnx,data.camera_id)
                return data
        except:
                cnx.reconnect()
                data= GetKafkaDataByCamid.get_data(cnx,data.camera_id)
                cnx.cmd_refresh(1)
                return data

# @app.post("/modelvalidate")
# async def model_validate_fetch(data: ModelValidation):
#                 try:
#                         cnx.cmd_refresh(1)
#                         data = ValidationModel.get_data(validateconfig,
#                                         data.model_id, data.framework_id)
#                         print("=========",data)
#                         return data
#                 except:
#                         cnx.reconnect()
#                         cnx.cmd_refresh(1)
#                         data = ValidationModel.get_data(validateconfig,
#                                         data.model_id, data.framework_id)
#                         return data
                

@app.get("/ports")
async def model_ports_fetch(data: ModelPorts):
#     cnx=connection_sql()
#     cnx = cnxpool.get_connection()
    print("data ",data.model_id)
    try:
        cnx.cmd_refresh(1)
        data = GetPortDetails.get_data(cnx,data.model_id)
        return data
    except:
        cnx.reconnect()
        cnx.cmd_refresh(1)
        data = GetPortDetails.get_data(cnx,data.model_id)
        return data
    
#     cnx.close()
        
    
@app.post("/updateports")
async def model_ports_update(data: ModelPorts):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()
        print("in update port ",data.model_port,data.model_id)
        try:
                cnx.cmd_refresh(1)
                data = UpdateModelPort.update(cnx,data.model_port,data.model_id)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = UpdateModelPort.update(cnx,data.model_port,data.model_id)
                # cnx.close()
                return data
        
@app.post("/updatemodelstatus")
async def model_status_update(data: ModelStatus):
        
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()
        print("in update model status ",data.model_id, data.status, data.message)
        try:
                cnx.cmd_refresh(1)
                data = UpdateModelStatus.update(cnx,data.model_id, data.status,data.message)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = UpdateModelStatus.update(cnx,data.model_id, data.status,data.message)
                # cnx.close()
                return data
        

@app.get("/summarytime")
async def summary_time_fetch():
#     cnx=connection_sql()
    try:
        cnx.cmd_refresh(1)
        data = GetSummaryTimeDetails.get_data(cnx)
        #     cnx.close()
        return data
    except:
        cnx.reconnect()
        data = GetSummaryTimeDetails.get_data(cnx)
        #     cnx.close()
        return data
@app.post("/updatesummarytime")
async def summary_time_update(data: SummaryTime):
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()
        try:
                cnx.cmd_refresh(1)
                print("in update summary time ",data.start_time,data.end_time)
                data = UpdateIncidentSummaryTime.update(cnx, data.start_time, data.end_time)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                print("in update summary time ",data.start_time,data.end_time)
                data = UpdateIncidentSummaryTime.update(cnx, data.start_time, data.end_time)
                # cnx.close()
                return data
        
@app.post("/preview")  # getCameraFrame
async def CameraFrame_fetch(data: CameraDetails):
        print("============camera data =================")
        print(data)
        try:
                cnx.cmd_refresh(1)
                return GetCameraFrames.get_desired_frames(
                        data.rtsp_url, data.username, data.password
                )
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                return GetCameraFrames.get_desired_frames(
                        data.rtsp_url, data.username, data.password
                )

@app.get("/getincidentvideoconf") 
async def Incident_details_fetch(data: IncidentVideo):
        print("*"*10)
        print(data)
        print(data.incident_video_id)
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()
        try:
                cnx.cmd_refresh(1)
                data = GetIncidentVideoData.get_data(cnx,
                        data.incident_video_id
                )
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = GetIncidentVideoData.get_data(cnx,
                        data.incident_video_id
                )
                # cnx.close()
                return data
        
@app.post("/updateincidentvideoconf") 
async def Incident_details_fetch(data: UpdateIncidentVideo):
        print("*"*10)
        print(data)
        print(data.incident_video_id)
        # cnx=connection_sql()
        # cnx = cnxpool.get_connection()
        try:
                cnx.cmd_refresh(1)
                data = UpdateIncidentVideoStatus.update(cnx,
                        data.incident_video_id,
                        data.status,
                        data.message
                )
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = UpdateIncidentVideoStatus.update(cnx,
                        data.incident_video_id,
                        data.status,
                        data.message
                )
                # cnx.close()
                return data

@app.get("/geteventnotification") 
async def event_notification_details(data: notification_config):
        # cnx=connection_sql()
        try:
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_eventbased_notification_data(cnx,
                        data.camera_id,data.usecase_id)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_eventbased_notification_data(cnx,
                        data.camera_id,data.usecase_id)
                # cnx.close()
                return data

@app.get("/gethournotification") 
async def event_notification_details(data: notification_config):
        # cnx=connection_sql()
        try:
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_hourly_notification_data(cnx,
                        data.camera_id,data.usecase_id)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_hourly_notification_data(cnx,
                        data.camera_id,data.usecase_id)
                # cnx.close()
                return data

@app.get("/getendofshiftnotification") 
async def event_notification_details(data: notification_config):
        # cnx=connection_sql()
        try:
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_endshiftbased_data(cnx,
                        data.camera_id,data.usecase_id)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_endshiftbased_data(cnx,
                        data.camera_id,data.usecase_id)
                # cnx.close()
                return data

@app.get("/getnotificationdetails") 
async def event_notification_details(data: camera_config):
        # cnx=connection_sql()
        try:
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_notification_data_bycameraid(cnx,
                        data.camera_id)
                # cnx.close()
                return data
        except:
                cnx.reconnect()
                cnx.cmd_refresh(1)
                data = GetNotificationDetails.get_notification_data_bycameraid(cnx,
                        data.camera_id)
                # cnx.close()
                return data