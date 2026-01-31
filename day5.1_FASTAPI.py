from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


users = []



class UserCreate(BaseModel):
    username: str
    age: int



@app.get("/")
def home():
    return {"message": "Backend is working"}



@app.get("/users")
def get_users():
    return {
        "count": len(users),
        "users": users
    }



@app.post("/users")
def create_user(user: UserCreate):

    
    if len(user.username) < 3:
        return {"status": "error", "message": "username must be at least 3 characters"}

    if user.age < 0:
        return {"status": "error", "message": "age must be positive"}

    
    new_user = {
        "username": user.username,
        "age": user.age
    }


    users.append(new_user)


    return {
        "status": "ok",
        "data": new_user
    }
