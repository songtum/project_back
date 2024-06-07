# todo.py
from fastapi import APIRouter, Path
from model import GuestbookEntry
from datetime import datetime

guestbook_router = APIRouter()

guestbook_list = []
guestbook_counter = 0

@guestbook_router.post("/guestbook")
async def add_guestbook_entry(entry: GuestbookEntry) -> dict:
    global guestbook_counter
    entry.id = guestbook_counter = guestbook_counter + 1
    entry.timestamp = datetime.now()
    guestbook_list.append(entry)
    return {"msg": "Guestbook entry added successfully"}

@guestbook_router.get("/guestbook")
async def retrieve_guestbook_entries() -> dict:
    return {"entries": guestbook_list}

@guestbook_router.delete("/guestbook/{entry_id}")
async def delete_guestbook_entry(entry_id: int = Path(..., title="the ID of the entry to delete")) -> dict:
    for index, entry in enumerate(guestbook_list):
        if entry.id == entry_id:
            del guestbook_list[index]
            return {"msg": f"Entry with ID {entry_id} deleted successfully"}
    return {"msg": "Entry with supplied ID doesn't exist"}
