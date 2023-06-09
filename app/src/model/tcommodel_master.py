from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
class ModelMasterEndpoint(BaseModel):
    model_end_point: Union[str, None] = None
    model_id: Union[str, None] = None

class Tcom_Model_Master_Model(BaseModel):
    model_id: Union[int, None] = None
    batchsize:  Union[int, None] = None
    created_by: Union[str, None] = None
    created_on: Union[str, None] = None
    device: Union[str, None] = None
    model_description: Union[str, None] = None
    model_end_point: Union[str, None] = None
    model_framework: Union[str, None] = None
    model_name: Union[str, None] = None
    model_type: Union[str, None] = None
    updated_on: Union[str, None] = None
    usecase_id: Union[str, None] = None