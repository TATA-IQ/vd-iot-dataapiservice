from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

# @validate_call
class ModelValidation(BaseModel):
    # model_id: Union[str, None] = None
    # framework_id: Union[str, None] = None
    model_id: Union[int, None] = None
    framework_id: Union[int, None] = None