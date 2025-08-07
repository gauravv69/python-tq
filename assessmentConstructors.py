'''
Create a class Product, assign value for product id, name, price

If price is >2000  → 20% discount
If price 1000- 2000  → 10% discount
Price <1000           → 5% discount

Display id, name actual price & discounted price 
'''
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price
        self.discounted_price = self.discount()
        
    def discount(self):
        if self.price > 2000:
            return self.price - (self.price * 0.20)
        elif self.price >= 1000:
            return self.price - (self.price * 0.10)
        else:
            return self.price - (self.price * 0.05)
        
    def display(self):
        print("Product Id:",self.pid)
        print("Name:",self.name)
        print("Actual Price:",self.price)
        print(f"Discounted Price: {self.discounted_price}")
        
p1 = Product(1, "Cricket Bat", 2500)
p1.display()
print("-----*****-----")
p2 = Product(2, "Leather Ball", 2500)
p2.display()
print("-----*****-----")





'''
Create a class Circle accept the value of radius & initialise using initializer
Calculate the area of circle
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area_circle(self):
        area = 3.14 * self.radius * self.radius
        return area
    
    def display(self):
        print("Radius:",self.radius)
        print("Area of circle:",self.area_circle())
        
c1 = Circle(5)
c1.display()







'''
Create a class IncomeTax

Accept the annual income

0- 5lcs  → 0 % tax
5- 10  → 20% tax
10-15 → 40%
Above 15 → 45 % tax

Display name of person, annual income  & tax amount to pay
'''
class IncomeTax:
    def __init__(self, name, annual_income):
        self.name = name
        self.annual_income = annual_income
        
    def total_tax(self):
        income = self.annual_income
        if income <= 500000:
            self.tax = 0
        elif income <= 1000000:
            self.tax =  income * 0.20
        elif income <= 1500000:
            self.tax = income * 0.40
        else:
            self.tax = income * 0.45
        
    def display(self):
        print("Name of Person:",self.name)
        print("Annual Income:",self.annual_income)
        print("Tax amt to Pay:",self.tax)
        

print("-----*****-----")        
person1 = IncomeTax("Gaurav", 450000)
person1.total_tax()
person1.display() 
        
























        
