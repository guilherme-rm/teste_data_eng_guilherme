# schemas.py
from pydantic import BaseModel
from datetime import datetime

class input(BaseModel):
    timestamp: datetime
    names: list
