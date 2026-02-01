from fastapi  import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []



class UserCreate(BaseModel):
    username: str
    age: int


@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.post("/users")
def create_user(user: UserCreate):
    new_user = {"username": user.username, "age": user.age}
    users.append(new_user)
    return {"status": "ok", "data": new_user}



@app.get("/users")
def get_users():
    return {"count": len(users), "users": users}

@app.get("/users/{username}")

def get_user(username: str):
    for user in users:
        if user["username"].lower() == username.lower():
            return {"status":"ok", "data": user}
        
        return {"status":"error", "message": "User not found"}
    
