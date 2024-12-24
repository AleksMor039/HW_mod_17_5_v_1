from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship  # взаимосвязь
from app.models import *

'''
В user.py создать модель User, 
наслед. от ранее написанного Base со следующими атрибутами:
'''


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    # relationship - показ.взаимосвязь (к кому взаимосвязь) и (куда возвращаться с ней)
    # объект связи с табл. Task
    tasks = relationship("Task", back_populates="user")


# from sqlalchemy.schema import CreateTable

# print(CreateTable(User.__table__))
