class Emp:

    def __init__(self, id, name, sal):
        self.id = id
        self.nm = name
        self.salary = sal
        print("Hey, I am Constructor!")

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




    def display(self):
        print("\n----- Employee Details -----")
        print(f"ID     : {self.getId()}")
        print(f"Name   : {self.getName()}")
        print(f"Salary : {self.getSalary()}")
        print("----------------------------")


e = Emp(101, "Joe", 25000)
e.setName("Rishi")

r = e.getSalary()
print(r)

print(e.getName())  # print old name i.e Rishi

e.setName("Ishan")  # print update name that is Ishan

e.display()


# self is nothing but object 
# why we use self keyword -> bcz we can not accsess directly.





