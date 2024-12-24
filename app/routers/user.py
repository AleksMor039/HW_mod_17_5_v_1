from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# ф-ия подкл. БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic
from typing import Annotated
from app.models import *
from app.schemas import CreateUser, UpdateUser, CreateTask
# ф-ия работы с записями
from sqlalchemy import insert, select, update, delete
# функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_user(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get('/user_id/{user_id}')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'

        )
    return user


@router.post('/create')
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    # Проверка на существование пользователя
    found_user = db.scalar(select(User).where(User.username == user.username))
    if found_user is not None:
        raise HTTPException(status_code=400, detail="User  with this username already exists")

    # Создание нового пользователя
    db.execute(insert(User).values(username=user.username,
                                   firstname=user.firstname,
                                   lastname=user.lastname,
                                   age=user.age,
                                   slug=slugify(user.username)))

    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Succesful'
    }


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, update_user: UpdateUser):
    # провеерка существования пользователя
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'

        )
    # Обновление данных пользователя
    db.execute(update(User).where(User.id == user_id).values(
        firstname=update_user.firstname,
        slug=slugify(update_user.firstname),
        lastname=update_user.lastname,
        age=update_user.age,
    ))

    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is succesful'
    }


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'

        )
    # Удал.всех задач связанных с пользователем
    db.execute(delete(Task).where(Task.user_id == user_id))
    # Удал.пользователя
    db.execute(delete(User).where(User.id == user_id))

    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is succesful'
    }

'''
нов. маршрут - логика - возвр.всех Task конкретного User по id
'''
@router.get('/{user_id}/tasks')
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    return tasks
