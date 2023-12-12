from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class CameraDetails(BaseModel):
    rtsp_ip: Union[str, None] = None
    rtsp_url: Union[str, None] = None
    username: Union[str, None] = None
    password: Union[str, None] = None


class CameraConfig(BaseModel):
    camera_group_id: Union[tuple, None] = None
    location_id: Union[tuple, None] = None
    customer_id: Union[tuple, None] = None
    subsite_id: Union[tuple, None] = None
