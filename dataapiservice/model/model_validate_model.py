from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
class ModelValidation(BaseModel):
    model_id: Union[int, str]
    framework: str