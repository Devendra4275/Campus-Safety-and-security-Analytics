from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    description = Column(String, nullable=True)
