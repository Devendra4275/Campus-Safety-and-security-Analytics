from pydantic import BaseModel
from datetime import datetime

class IncidentCreate(BaseModel):
    type: str
    location: str
    time: datetime
    description: str

class IncidentResponse(BaseModel):
    id: int
    type: str
    location: str
    time: datetime
    description: str

    class Config:
        orm_mode = True
