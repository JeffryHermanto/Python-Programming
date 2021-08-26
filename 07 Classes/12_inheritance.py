# Inheritance

class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
