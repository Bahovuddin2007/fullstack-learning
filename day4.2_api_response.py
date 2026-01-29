users = []


def success(data):
    return {
        "status": "ok",
        "data": data
    }


def error(message):
    return {
        "status": "error",
        "message": message
    }


def create_user(name, age):
    # validation
    if not name:
        return error("Name is required")

    if not isinstance(age, int):
        return error("Age must be an integer")

    if age < 0:
        return error("Age must be positive")

    # create + save
    user = {"name": name, "age": age}
    users.append(user)

    return success(user)


def get_users():
    return success(users)


def get_user_by_name(name):
    if not name:
        return error("Name is required")

    for user in users:
        if user["name"].lower() == name.lower():
            return success(user)

    return error("User not found")


def get_adults():
    adults = []
    for user in users:
        if user["age"] >= 18:
            adults.append(user)

    return success(adults)


print("-create users-")
print(create_user("baha", 20))
print(create_user("anna", 17))
print(create_user("", 25))    
print(create_user("amira", -1))  
print(create_user("thor", "18")) 

print("\n-adults-")
print(get_users())

print("\n-get user by name-")
print(get_user_by_name("amira"))
print(get_user_by_name("Unknown")) 

print("\n-adults-")
print(get_adults())
