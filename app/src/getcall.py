from src.getdata.tcomclass_master import GetClassMaster
from src.getdata.tcommodel_cameragroup import GetModelCamGroup
from src.getdata.tcommodel_classlink import GetModelClassLink
from src.getdata.tcommodel_config import GetModelConfig
from src.getdata.tcommodel_framework import GetModelFramework
from src.getdata.tcommodel_master import GetModelMaster
from src.getdata.tcommodel_type import GetModelType

class ClassMaster():
    def __init__(self,app):
        self.app=app
    @self.app.get("/get")
    async def fetch():
        GetClassMaster.get_data()
'''
class ModelCameraGroup():
    async def fetch():
        GetModelCamGroup.get_data()

class ModelClassLink():
    async def fetch():
        GetModelClassLink.get_data()
class ModelConfig():
    def fetch():
        GetModelConfig.get_data()




class ModelType():
    def fetch():

        GetModelType.get_data()


'''