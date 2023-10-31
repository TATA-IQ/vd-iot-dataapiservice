from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class ScheduleMaster(BaseModel):
    
    camera_group_id: Union[tuple, None] = None
    