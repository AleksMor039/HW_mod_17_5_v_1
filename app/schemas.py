from pydantic import BaseModel

'''
Создали 4 схемы в schemas.py, наследуемые от BaseModel, 
для удобной работы с будущими объектами БД
'''
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
