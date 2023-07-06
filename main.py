
from typing import Union
from fastapi import FastAPI

from ArdDatabase.database import Database

app = FastAPI()

db = Database().instance()

@app.get("/video/random/")
def random_videos(category: Union[str, None]= None, number: int = 0):
    if category is None:
        return db.get_random_videos(number)
    return db.get_random_videos_category(category, number)

