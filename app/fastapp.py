from fastapi import FastAPI
from config_parser.parser import ParseConfig
import logging
from logging.handlers import TimedRotatingFileHandler
from src.getdata import *
#from src.getcall import *
from src.postdata.tcommodel_master_post import UpdateEndPoint, Insert_Tcom_Model_Master
from src.postdata.tcom_usecase_post import Tcom_Usecase_Insert
from src.getdata.tcomclass_master import GetClassMaster
from src.getdata.tcommodel_cameragroup import GetModelCamGroup
from src.getdata.tcommodel_classlink import GetModelClassLink
from src.getdata.tcommodel_config import GetModelConfig,GetModelConfigById
from src.getdata.tcommodel_framework import GetModelFramework
from src.getdata.tcommodel_master import GetModelMaster,GetModelMasterById
from src.getdata.tcommodel_type import GetModelType
from src.getdata.tcomuse_case import GetUseCase
from src.getdata.tcomuse_case_customer import GetUseCaseCustomer
from src.getdata.tcommodel_customer import GetCustomer
from src.docker.containerinsert import InsertContainer,InsertContainerModel
from src.model.container_model import Container_Model,Container_Model_Exist_Query,ContainerModelQueryName,ContainerModelQueryId,ContainerModelQueryModelId
from src.model.container import  Container,ContainerQueryId,ContainerQueryUpdateId,ContainerQueryName
from src.docker.containerselect import ExistContainerByName, GetContainerByContainerid, GetContainerModelByModelId, GetContainerModel,ExistContainerModelByName
from src.docker.containerupdate import UpdateContainer
from src.model.tcommodel_master import  Tcom_Model_Master_Model,ModelMasterEndpoint
from src.model.tcom_use_case import Tcom_Use_Case_Model
from src.model.tcommodel_config import Tcom_Model_Config
import mysql.connector
logger = logging.getLogger("Rotating Log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.setLevel(logging.ERROR)

handler = TimedRotatingFileHandler("logs/log", 'D', 1, 7)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.log(40,msg="Database Started")

dbconfig= ParseConfig.getDBConfig()
# enginecls=Engine(dbconfig["host"],dbconfig["username"],dbconfig["password"],dbconfig["db"])
# engineobj,metadata=enginecls.create_engine()
cnx = mysql.connector.connect(user=dbconfig["username"], password=dbconfig["password"],
                              host=dbconfig["host"],
                              database=dbconfig["db"])
app = FastAPI()
@app.get("/getClassMaster")
async def ClassMaster_fetch():
        GetClassMaster.get_data(cnx)

@app.get("/getModelCameraGroup")
async def ModelCameraGroup_fetch():
        return GetModelCamGroup.get_data(cnx)

@app.get("/getModelClassLink")
async def ModelClassLink_fetch():
        return GetModelClassLink.get_data(cnx)

@app.get("/getModelFramework")
async def ModelFramework_fetch():
        return GetModelFramework.get_data(cnx)

@app.get("/getModelMaster")
async def ModelMaster_fetch():
        return GetModelMaster.get_data(cnx)
@app.get("/getModelMasterbyId")
async def ModelMasterById_fetch(data:Tcom_Model_Master_Model):
        return GetModelMasterById.get_data(cnx,data.model_id)

@app.get("/getModelConfig")
async def ModelConfig_fetch():
        return GetModelConfig.get_data(cnx)

@app.get("/getModelConfigbyId")
async def ModelConfigById_fetch(data:Tcom_Model_Config):
        
        if data.location_id != None  and data.model_id!=None:
                return GetModelConfigById.get_data(cnx,data.model_id,data.location_id)
        else:
                return GetModelConfigById.get_data(cnx,data.model_id)


@app.get("/getModelType")  
async def ModelType_fetch():

        return GetModelType.get_data(cnx)


@app.get("/getCustomer")  
async def Customer_fetch():

        return GetCustomer.get_data(cnx)

@app.get("/getUseCase")  
async def UseCase_fetch():
# /home/aditya.singh/Pocs/vision/database
        return GetUseCase.get_data(cnx)
@app.get("/getUseCaseCustomer")  
async def UseCaseCustomer_fetch():

        return GetUseCaseCustomer.get_data(cnx)


@app.get("/container")
async def Container_Fetch(data:ContainerQueryId):
        print("")
        print("data==>",data)
        return GetContainerByContainerid.get_data(cnx,data.container_id)
@app.get("/containermodel")
async def ContainerModel_Fetch(data:ContainerModelQueryModelId):
        return GetContainerModelByModelId.get_data(cnx,data.model_id)

@app.get("/existContainerName")
async def ContainerByName_Exist(data:ContainerQueryName):
        return ExistContainerByName.get_data(cnx,data.container_name)
@app.get("/existContainerId")
async def ContainerByName_Exist(data:ContainerQueryId):
        return ExistContainerById.get_data(cnx,data.container_id)

@app.get("/existContainerModelName")
async def ContainerByName_Exist(data:ContainerModelQueryName):
        return ExistContainerModelByName.get_data(cnx,data.container_name)
@app.get("/existContainerModelId")
async def ContainerByName_Exist(data:ContainerModelQueryName):
        if ContainerModelQueryName["container_id"] is not None:
                return ExistContainerModelById.get_data(cnx,data.container_id)
        if ContainerModelQueryName["model_id"] is not None:
                return ExistContainerModelByModel.get_data(cnx,data.model_id)

@app.post("/insertContainer")
async def Container_Insert(data:Container):
        print("========")
        print(data)
        return InsertContainer.insert(cnx,data)


@app.post("/insertContainerModel")
async def ContainerModel_Insert(data:Container_Model):
        print("======>","insertcontainer Model",data)
        return InsertContainerModel.insert(cnx,data)


@app.post("/updateContainer")
async def ContainerModel_Insert(data:ContainerQueryUpdateId):
        return UpdateContainer.update(cnx,data.container_id,data.container_name)

@app.post("/updateEndpoint")
async def Endpoint_Update(data:ModelMasterEndpoint):

        print("update===>",data)
        print("*******",data.model_end_point)
        print("*******",data.model_id)
        return UpdateEndPoint.update(cnx,data.model_end_point,data.model_id)

@app.post("/insertModelMaster")
async def ModelMaster_Insert(data:Tcom_Model_Master_Model):
        print(data)
        return Insert_Tcom_Model_Master.insert(cnx,data)
@app.post("/insertUsecase")
async def Usecase_Insert(data:Tcom_Use_Case_Model):
        print(data)
        return Tcom_Usecase_Insert.insert(cnx,data)