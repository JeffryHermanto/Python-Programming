# Multi-level Inheritance

# Limit using it to 1-2 levels

class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


# Example of inheritance abuse
class Chicken(Bird):
    pass
