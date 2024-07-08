from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Revenue(Base):
    __tablename__ = 'revenue'

    month = Column(String, primary_key=True, index=True)
    revenue = Column(Integer, index=True)
