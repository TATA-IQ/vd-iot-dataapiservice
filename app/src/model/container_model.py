from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Container_Model(BaseModel):
    container_name: Union[str, None] = None
    container_tag: Union[str, None] = None
    model_id: Union[str, None] = None
    model_usecase: Union[str, None] = None
    model_path: Union[str, None] = None
    model_port: Union[str, None] = None
    model_framework: Union[str, None] = None
    file_name:Union[str, None] = None

class Container_Model_Exist_Query(BaseModel):
    container_name: Union[str, None] = None
    container_tag: Union[str, None] = None
    model_id: Union[str, None] = None
    model_usecase: Union[str, None] = None
    model_path: Union[str, None] = None
    model_port: Union[str, None] = None
    model_framework: Union[str, None] = None
    file_name:Union[str, None] = None

class ContainerModelQueryId(BaseModel):
    container_id: Union[str, None] = None

class ContainerModelQueryName(BaseModel):
    container_name: Union[str, None] = None
class ContainerModelQueryModelId(BaseModel):
    model_id: Union[str, None] = None