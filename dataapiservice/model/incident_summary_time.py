from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union


class SummaryTime(BaseModel):
    
    start_time: Union[str, None] = None
    end_time: Union[str, None] = None
    