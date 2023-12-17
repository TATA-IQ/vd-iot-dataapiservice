from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class CameraGroup(BaseModel):
    location_id: Union[tuple, None] = None
    camera_group_id: Union[tuple, None] = None
    customer_id: Union[tuple, None] = None
    subsite_id: Union[tuple, None] = None
    zone_id: Union[tuple, None] = None

class CameraIDs(BaseModel):
    location_id: Union[tuple, None] = None
    camera_group_id: Union[tuple, None] = None
    customer_id: Union[tuple, None] = None
    subsite_id: Union[tuple, None] = None
    zone_id: Union[tuple, None] = None
    camera_group_id: Union[tuple, None] = None
