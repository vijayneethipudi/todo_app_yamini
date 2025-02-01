from typing import Any, Dict, List, Union

from fastapi import APIRouter

router = APIRouter(prefix="/todos", tags=["todos"], responses={404: {"description": "Not Found"}})


@router.get("/")
def get_all_todos():
    pass


@router.get("/{todo_id}")
def get_todo_by_id():
    pass


@router.post("/")
def create_todo():
    pass


@router.put("/{todo_id}")
def update_todo():
    pass


@router.delete("/{todo_id}")
def delete_todo():
    pass
