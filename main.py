
from fastapi import FastAPI

from ArdDatabase.database import Database

app = FastAPI()

db = Database().instance()

@app.get("/video/random/{number}")
def read_root(number: int):
    return db.get_random_videos(number)

