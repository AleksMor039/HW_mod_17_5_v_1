from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship  # взаимосвязь
from app.models import *

'''
В task.py создать модель Task, 
наслед. от ранее написанного Base с атрибутами
'''


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    # relationship - показ.взаимосвязь (к кому взаимосвязь) и (куда возвращаться с ней)
    # объект связи с табл. User
    user = relationship("User", back_populates="tasks")


# from sqlalchemy.schema import CreateTable

# print(CreateTable(Task.__table__))
