# Method Overriding

class Animal:
    def __init__(self) -> None:
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self) -> None:
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
