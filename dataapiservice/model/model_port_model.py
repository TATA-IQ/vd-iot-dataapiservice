from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class ModelPorts(BaseModel):
    
    model_id: Union[int, None] = None
    model_port: Union[int, None] = None
    