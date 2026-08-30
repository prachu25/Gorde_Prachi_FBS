from abc import ABC, abstractmethod
class EmpInherit(ABC):

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.salary = sal


    # getter and setter
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id 

    
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name =  name

    
    def getSalary(self):
        return self.salary
        
    def setSalary(self, salary):
        self.salary = salary

    @abstractmethod
    def CalulateSalary(self):
        print(' I am from Emp Salary ')

    # str method print the obj of class
    # where the str method is store? 
    # ans: in object class i.e cosmic super class
    def __str__(self):
        return f"ID: {self.id} \t Name: {self.name} \t Salary: {self.salary}"


#------------------------------------------------------------------------------



class Hr(EmpInherit):

    def __init__(self, id, name, sal, commision):
        super().__init__(id, name, sal)
        self.commi = commision

    def getCommision(self):
        return self.commi

    def setCommision(self, commi):
        self.commi = commi

    def CalulateSalary(self):
        pass

    def __str__(self):
        return super().__str__() + f" \tCommision: {self.commi}"


# ----------------------------------------------------------------------------

class Dev(EmpInherit):

    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)

        self.bonus = bonus


    # getter and setter

    def getBonus(self):
        return self.bonus

    def setBonus(self, bonus):
        self.bonus = bonus

    def CalulateSalary(self):
        print('I am from Dev salary')

    def __str__(self):
        return super().__str__() + f" \tBonus: {self.bonus}"
    
    



# we can not create a Obj of Emp bcz its is abstract class

# Object of Parent Class
# emp1 = EmpInherit(101, "Rahul", 50000)

# print("\nDisplay __str__ Method \n")
# print(emp1)


# Object of Hr Class
hr1 = Hr(102, "Priya", 60000, 5000)
print(hr1)



# Object of Dev Class
dev1 = Dev(103, "Amit", 70000, 10000)
print(dev1)
    


    

