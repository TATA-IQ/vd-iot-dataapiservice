from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
class Tcom_Use_Case_Model(BaseModel):
    usecase_id: Union[int, None] = None
    created_by: Union[str, None] = None
    created_on: Union[str, None] = None
    updated_by: Union[str, None] = None
    updated_on: Union[str, None] = None
    use_case_description: Union[str, None] = None
    usecase_name: Union[str, None] = None
    