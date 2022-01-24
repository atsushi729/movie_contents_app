from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
# from app.users.models import User
# from app import config, db

app = FastAPI()
# settings = config.get_setting()


@app.on_event("startup")
def on_startup():
    print("hello world")
    # db.get_session()
    # sync_table(User)


@app.get("/")
def homepage():
    return {"hello": "world"}
