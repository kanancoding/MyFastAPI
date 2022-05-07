from datetime import datetime
from decimal import Decimal
from numpy import str_
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, DECIMAL
from sqlalchemy.sql import func

from decimal import Decimal

from tables import Col
from models.database import Base
from pydantic import BaseModel

class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index = True)
    username = Column(String,unique=True)
    password = Column(String)
    created_date = Column(DateTime(timezone=True),server_default=func.now())

class UserBase(BaseModel):
    username: str
    password: str

class UserDisplayBase(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True

