from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class Tcom_Model_Config(BaseModel):
    model_id: Union[int, None] = None
    location_id: Union[int, None] = None