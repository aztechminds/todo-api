from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class TodoCreate(BaseModel):
    id: int
    title: str
    status: bool = False


class Todo(BaseModel):
    id: int
    title: str
    status: bool = False

app = FastAPI()

todos=[]

@app.get("/")
def root():
    return "Hello Abdullah"

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos", response_model=List[Todo])
def post_todos(todo: TodoCreate):
    new_todo = Todo(
        id = todo.id,
        title=todo.title,
        status=todo.status
    )
    todos.append(new_todo)
    return todos