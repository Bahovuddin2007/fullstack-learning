from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# "База" пока в памяти (список)
users = []


# --------- МОДЕЛИ (Pydantic) ---------
class UserCreate(BaseModel):
    username: str
    age: int


class UserUpdate(BaseModel):
    age: int


# --------- ВСПОМОГАТЕЛЬНОЕ ---------
def find_user_index(username: str) -> int:
    """Ищем индекс юзера по username (без учета регистра)."""
    for i, u in enumerate(users):
        if u["username"].lower() == username.lower():
            return i
    return -1


# --------- РОУТЫ ---------
@app.get("/")
def home():
    return {"message": "Day 12 CRUD is working"}


# CREATE
@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    # валидации
    if len(user.username) < 3:
        raise HTTPException(status_code=400, detail="Username must be at least 3 characters")

    if user.age < 0 or user.age > 100:
        raise HTTPException(status_code=400, detail="Age must be between 0 and 100")

    # проверка на дубликат
    if find_user_index(user.username) != -1:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = {"username": user.username, "age": user.age}
    users.append(new_user)

    return {"status": "ok", "data": new_user}


# READ ALL
@app.get("/users")
def get_users():
    return {"count": len(users), "users": users}


# READ ONE
@app.get("/users/{username}")
def get_user(username: str):
    idx = find_user_index(username)
    if idx == -1:
        raise HTTPException(status_code=404, detail="User not found")

    return {"status": "ok", "data": users[idx]}


# UPDATE (меняем возраст)
@app.put("/users/{username}")
def update_user(username: str, data: UserUpdate):
    idx = find_user_index(username)
    if idx == -1:
        raise HTTPException(status_code=404, detail="User not found")

    if data.age < 0 or data.age > 100:
        raise HTTPException(status_code=400, detail="Age must be between 0 and 100")

    users[idx]["age"] = data.age
    return {"status": "ok", "data": users[idx]}


# DELETE
@app.delete("/users/{username}")
def delete_user(username: str):
    idx = find_user_index(username)
    if idx == -1:
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = users.pop(idx)
    return {"status": "ok", "deleted": deleted_user}
