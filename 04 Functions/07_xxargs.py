# xxargs

def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=1, name="Jeffry", age=43)
