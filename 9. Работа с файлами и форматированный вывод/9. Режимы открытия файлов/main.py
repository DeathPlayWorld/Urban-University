

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f"{self.name}, {self.weight}, {self.category}")

class Shop:
    __file_name = "product.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        string = file.read()
        file.close()
        return str(string)

    def add(self, *products):
        file = open(self.__file_name, "r")
        for i in range(0, len(products)):
            if str(products[i]) in self.get_products():
                print(f"Product {products[i]} already in the shop!")
            else:
                file = open(self.__file_name, "a")
                file.write(f"{products[i]}\n")
                file = open(self.__file_name, "r")
        file.close()

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)

print(s1.get_products())
