from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class notification_config(BaseModel):
    camera_id: Union[int, None] = None
    usecase_id: Union[int, None] = None
    
class camera_config(BaseModel):
    camera_id: Union[int, None] = None