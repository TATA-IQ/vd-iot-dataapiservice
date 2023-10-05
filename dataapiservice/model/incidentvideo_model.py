from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

class IncidentVideo(BaseModel):
    incident_video_id: Union[str, None] = None