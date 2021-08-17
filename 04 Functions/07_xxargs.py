# xxargs

def saveUser(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


saveUser(id=1, name="Jeffry", age=43)
