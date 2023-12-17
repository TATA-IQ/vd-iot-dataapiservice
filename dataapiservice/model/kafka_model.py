from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
class KafkaTopics(BaseModel):
    
    camera_group_id: Union[tuple, None] = None
class KafkaTopicsCamId(BaseModel):
    
    camera_id: Union[tuple, None] = None
    