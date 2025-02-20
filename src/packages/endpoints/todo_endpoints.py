import logging
from typing import Any, Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from packages.database.database import Base, engine, get_db
from packages.helpers.todo_crud import TodoCrud
from packages.models import todo_schemas

Base.metadata.create_all(bind=engine)  # it creates if the tables are not availble in the database based on the schema

router = APIRouter(prefix="/todos", tags=["todos"], responses={404: {"description": "Not Found"}})


@router.get("/")
def get_all_todos(db: Session = Depends(get_db)):
    try:
        todo_obj = TodoCrud(db=db, logger=logging)
        return todo_obj.get_all_todos()
    except Exception as exc_info:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.get("/{todo_id}")
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    try:
        todo_obj = TodoCrud(db=db, logger=logging)
        return todo_obj.get_todo_by_id(todo_id)
    except Exception as exc_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc_info))


@router.post("/")
def create_todo(todo: todo_schemas.TodoCreate, db: Session = Depends(get_db)):
    try:
        todo_obj = TodoCrud(db=db, logger=logging)
        return todo_obj.create_todo(todo)
    except Exception as exc_info:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.put("/{todo_id}")
def update_todo(db: Session = Depends(get_db)):
    try:

        pass
    except Exception as exc_info:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))


@router.delete("/{todo_id}")
def delete_todo(db: Session = Depends(get_db)):
    try:
        pass
    except Exception as exc_info:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc_info))
