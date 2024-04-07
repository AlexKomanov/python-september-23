from fastapi import FastAPI
from models import User, Gender, Role
from uuid import uuid4, UUID

app = FastAPI()

users_db = [
    User(id=UUID("e3d9650d-5907-4daf-8760-f5343f121b7f"),
         first_name="Alex", last_name="Komanov",
         gender=Gender.male, roles=[Role.user, Role.admin]
         ),
    User(id=uuid4(), first_name="PLONI", last_name="PLONI", gender=Gender.female, roles=[Role.user, Role.student]),
    User(id=uuid4(), first_name="ALMONI", last_name="ALMONI", gender=Gender.female, roles=[Role.user, Role.guest]),
]


@app.get("/")
async def say_hello():
    return {
        "message": "Hello Alex!"
    }


@app.get("/api/v1/users")
async def get_all_users():
    return users_db
