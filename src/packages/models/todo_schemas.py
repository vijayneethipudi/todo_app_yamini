from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    """Todo Base class"""

    title: str
    description: str
    completed: bool


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    id: int


# Response model for todo Item
class TodoInDB(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True  # Tells the pydantic to treat SQLAlchemy models as dictionaries
