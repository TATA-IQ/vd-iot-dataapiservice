from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class Container(BaseModel):
    container_id: Union[str, None] = None
    container_name: Union[str, None] = None
    container_tag: Union[str, None] = None
    model_id: Union[str, None] = None

class ContainerQueryId(BaseModel):
    container_id: Union[str, None] = None

class ContainerQueryName(BaseModel):
    container_name: Union[str, None] = None

class ContainerQueryUpdateId(BaseModel):
    container_id: Union[str, None] = None
    container_name: Union[str, None] = None
    
