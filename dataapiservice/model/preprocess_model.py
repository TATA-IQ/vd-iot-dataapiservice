from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class PreprocessConfig(BaseModel):
    camera_group_id: Union[tuple, None] = None
class PreprocessConfigByid(BaseModel):
    preprocess_id: Union[tuple, None] = None
