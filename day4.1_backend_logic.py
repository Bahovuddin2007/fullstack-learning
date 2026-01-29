users = []

def create_user(name, age):
    if not name:
        return {"error": "Name is required"}

    if age < 0:
        return {"error": "Age must be positive"}

    user = {
        "name": name,
        "age": age
    }

    users.append(user)
    return user


def get_users():
    return users


def get_user_by_name(name):
    for user in users:
        if user["name"] == name:
            return user

    return {"error": "User not found"}



print(create_user("Ali", 20))
print(create_user("Bek", 17))
print(create_user("", 25))    
print(get_users())
print(get_user_by_name("Ali"))
print(get_user_by_name("John"))
