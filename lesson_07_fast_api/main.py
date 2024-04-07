from fastapi import FastAPI, HTTPException, status
from models import User, Gender, Role
from uuid import uuid4, UUID

app = FastAPI()

users_db = [
    User(id=UUID("e3d9650d-5907-4daf-8760-f5343f121b7f"),
         first_name="Alex", last_name="Komanov", middle_name="Victor",
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


@app.get("/api/v1/users/{user_id}")
async def get_single_user(user_id: UUID):
    for single_user in users_db:
        if single_user.id == user_id:
            return single_user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No user with id '{user_id}' was found..."
    )


@app.delete("/api/v1/users/{user_id}")
async def delete_particular_user(user_id: UUID):
    for single_user in users_db:
        if single_user.id == user_id:
            users_db.remove(single_user)
            return {
                "message": f"The user with id '{user_id}' was removed..."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No user with id '{user_id}' was found..."
    )


# @app.post("/api/v1/users", status_code=status.HTTP_201_CREATED)
# async def add_new_user(user: User):
#     users_db.append(user)
#     return {
#         "message": "A new user was created!",
#         "id": user.id
#     }

@app.post("/api/v1/users")
async def add_new_user(user: User):
    users_db.append(user)
    return {"message": "A new user was created", "id": user.id}
