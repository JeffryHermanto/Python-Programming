# The Object Class

class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
