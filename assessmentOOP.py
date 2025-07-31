'''
# Create Employee class , accept basic salary & allowances like HRA, DA, TA, PF
class Employee:
    def accept(self, basic_salary, hra, da, ta, pf):
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
        self.ta = ta
        self.pf = pf
        
    def display(self):
        print("Basic Salary:",self.basic_salary)
        print("HRA:",self.hra)
        print("DA:",self.da)
        print("TA:",self.ta)
        print("PF:",self.pf)
        
e1 = Employee()
e1.accept(80000, 10000, 8000, 5000, 2000)
e1.display()
'''



'''
# Calculate the gross salary & display Bs+allowances  - PF
class Employee:
    def accept(self, basic_salary, hra, da, ta, pf):
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
        self.ta = ta
        self.pf = pf
        
    def calculate_gross(self):
        gross_salary = self.basic_salary + self.hra + self.da + self.ta - self.pf
        return gross_salary
    
    def display(self):
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("TA:", self.ta)
        print("PF:", self.pf)
        print("Gross Salary:", self.calculate_gross())
        
e2 = Employee()
e2.accept(80000, 10000, 8000, 5000, 2000)
e2.calculate_gross()
e2.display()
'''




# Create two objects & display data for each object
class Employee:
    def accept(self, basic_salary, hra, da, ta, pf):
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
        self.ta = ta
        self.pf = pf
    
    def calculate_gross(self):
        gross_salary = self.basic_salary + self.hra + self.da + self.ta - self.pf
        return gross_salary
    
    def display(self):
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra)
        print("DA:", self.da)
        print("TA:", self.ta)
        print("PF:", self.pf)
        print("Gross Salary:", self.calculate_gross())
        
        
e3 = Employee()
e3.accept(80000, 10000, 8000, 5000, 2000)
e3.calculate_gross()
print("Employee ID 3 Details:")
e3.display()

e4 = Employee()
e4.accept(40000, 6000, 3000, 1500, 500)
e4.calculate_gross()
print("Employee ID 4 Details:")
e4.display()




