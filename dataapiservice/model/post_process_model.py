from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class PostProcessConf(BaseModel):
    usecase_id: Union[tuple, None] = None

class PostProcessClass(BaseModel):
    usecase_id: Union[int, None] = None
class PostProcessIncident(BaseModel):
    usecase_id: Union[int, None] = None
class PostProcessComputation(BaseModel):
    usecase_id: Union[int, None] = None
class PostProcessBoundary(BaseModel):
    usecase_id: Union[tuple, None] = None