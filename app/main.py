from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table

from app import config, db
from app.users.models import User


app = FastAPI()
DB_SESSION = None
# settings = config.get_setting()


@app.on_event("startup")
def on_startup():
    print("hello world")
    global DB_SESSION
    DB_SESSION = db.get_session()
    sync_table(User)


@app.get("/")
def homepage():
    return {"hello": "world"}

@app.get("/user")
def user_list_view():
    q = User.objects.all().limit(10)
    return list(q)

