
from typing import Union
from fastapi import FastAPI

from ArdDatabase.database import Database

app = FastAPI()

db = Database().instance()

@app.get("/video/random/{number}")
def read_root(number: int):
    videos = db.get_random_videos(number)
    if videos is not None:
        mp4s = []
        for video in videos:
            mp4 = video.video_url
            if mp4 is not None:
                mp4s.append(mp4)
        return mp4s
    return "no videos"


@app.get("/hello")
def read_item():
    return "hello"
