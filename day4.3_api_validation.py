

users = []

def success(data, status=200):
    return {
        "status_code": status,
        "data": data
    }


def error(message, status_code=400):
    return {
        "status_code": status_code,
        "error": message
    }


def create_user(username, age):

    if not username:
        return error("Username is required.", 422)

    if len(username) < 3:
        return error("Username must be at least 3 characters long.", 422)

    if not isinstance(age, int):
        return error("Age must be an integer.", 422)

    if age < 0:
        return error("Age must be a non-negative integer.", 422)

    if age > 100:
        return error("Age must be less than or equal to 100.", 422)

    user = {
        "username": username,
        "age": age
    }

    users.append(user)
    return success(user, 201)
