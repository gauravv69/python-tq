class Employee:
    def __init__(self, id, name, basic):
        self._id = id
        self._name = name
        self._basic = basic
        
    def calculate(self):
        self.hra = self._basic*0.40
        self.da = self._basic*0.20
        self.pf = self._basic*0.12
        self._gross=(self._basic + self.hra + self.da) - self.pf
        
    def __str__(self):
        return f"Employee Info \nID:{self._id} \nName:{self._name} \nGross Salary:{self._gross}"
    

class Manager(Employee):
    def __init__(self, id, name, basic, bonus):
        super().__init__(id, name, basic)
        self.__bonus = bonus
        
    def calculate(self):
        self.hra = self._basic*0.40
        self.da = self._basic*0.20
        self.pf = self._basic*0.12
        self._gross=(self._basic + self.hra + self.da + self.__bonus) - self.pf
        
    def __str__(self):
        return f"Manager Info \nID:{self._id} \nName:{self._name} \nGross Salary:{self._gross}"
    
    
'''
Class CEO (Employee):

         Implement the salary calculation for CEO

  Employee + ta + food  +basic+hra+da - pf
'''
    
class CEO(Employee):
    def __init__(self, id, name, basic, ta, food):
        super().__init__(id, name, basic)
        self.__ta = ta
        self.__food = food
    
    def calculate (self):
        self.hra = self._basic*0.40
        self.da = self._basic*0.20
        self.pf = self._basic*0.12
        self._gross=(self._basic + self.hra + self.da + self.__ta + self.__food) - self.pf
        
    def __str__(self):
        return f"CEO Info \nID:{self._id} \nName:{self._name} \nGross Salary:{self._gross}"
    

print("------CEO------")
c1 = CEO(101, "Gaurav", 50000, 10000, 8000)
c1.calculate()
print(c1)

print("------Manager------")
m1 = Manager(102, "Aditya", 100000, 6000)
m1.calculate()
print(m1)    

print("------Employee------")
e1 = Employee(103, "Raj", 60000)
e1.calculate()
print(e1)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        