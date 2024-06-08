# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from todo import guestbook_router
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5502", "http://34.239.34.113:8889"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome() -> dict:
    return {"msg": "Welcome to the guestbook API!"}

app.include_router(guestbook_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
