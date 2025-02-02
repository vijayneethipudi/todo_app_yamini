import logging
from typing import Any, Dict, List, Union

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from packages.models import todo_schemas, todo_tables


class TodoCrud:
    def __init__(self, db: Session, logger: logging.Logger):
        self.db = db
        self.logger = logger

    def get_all_todos(self) -> Union[List[todo_tables.TodoItem], None]:
        try:
            result = self.db.query(todo_tables.TodoItem).all()
            return result
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def get_todo_by_id(self, todo_id: int) -> Union[todo_tables.TodoItem, None]:
        try:
            result = self.db.query(todo_tables.TodoItem).filter(todo_tables.TodoItem.id == todo_id).first()
            if not result:
                raise Exception(f"Todo not found with id: {todo_id}")
            self.logger.info(f"Todo found with id: {todo_id}")
            return result
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def create_todo(self):
        try:
            pass
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def update_todo(self):
        try:
            pass
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info

    def delete_todo(self):
        try:
            pass
        except SQLAlchemyError as exc_info:
            raise exc_info
        except Exception as exc_info:
            raise exc_info
