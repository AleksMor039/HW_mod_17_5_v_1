from sqlalchemy import create_engine  # сущность, которая позволит запускать нашу БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

# создаём engine для связи с нашей БД
engine = create_engine("sqlite:///taskmanager.db", echo=True)  # создали движок

# создаём локальную сессию связи с нашей БД
SessionLocal = sessionmaker(bind=engine)  # bind - привязка и подтягиваем engine


# создаём класс будущей базы данных
class Base(DeclarativeBase):
    pass
