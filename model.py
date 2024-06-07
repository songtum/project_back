# model.py
from pydantic import BaseModel
from datetime import datetime

class GuestbookEntry(BaseModel):
    id: int = None
    author: str
    content: str
    timestamp: datetime = None

