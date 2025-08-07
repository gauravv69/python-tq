# Book → id, name, price
'''
Create setters & getters for book class & display the data
__str__ also to display book details
'''

class Book:
    __id = None
    __name = None
    __price = None

    # Setters
    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    # Getters
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def __str__(self):
        return f"Id = {self.__id}, Name = {self.__name}, Price = ₹{self.__price:.2f}"


b1 = Book()
b1.setId(201)
b1.setName("Mahabharat")
b1.setPrice(350.75)

print(b1)

print(b1.getId())
print("Book Name:", b1.getName())
print("Book Price: ₹", b1.getPrice())