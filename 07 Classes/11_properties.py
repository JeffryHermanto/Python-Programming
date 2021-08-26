# Properties

# class Product:
#     def __init__(self, price):
#         self.setPrice(price)

#     def getPrice(self):
#         return self.__price

#     def setPrice(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

#     price = property(getPrice, setPrice)

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(10)
print(product.price)

product.price = 50
print(product.price)
