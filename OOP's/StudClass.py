class Student:

    def __init__(self, roll_no, name, batch):
        self.roll_no = roll_no
        self.nm = name
        self.batch = batch 

        print("Hey, I am Student COnstructor!")

    def getRollNo(self):
        return self.roll_no

    def setRollNo(self,roll_no):
        self.roll_no = roll_no


    def getName(self):
        return self.nm
    
    def setName(self,name):
        self.nm = name

    def getBatch(self):
        return self.batch
    
    def setBatch(self,batch):
        self.batch  = batch
    


    def display(self):
        print("\n----- Student Details -----")
        print(f"Roll NO: {self.getRollNo()}")
        print(f"Name  : {self.getName()}")
        print(f"Btach : {self.getBatch()}")




# object creation
s = Student(101, "ROHIT", 4500)

print(s.getRollNo())

s.setName('Rishi')

# when we create object constructor automatically & print
# Hey, I am Student COnstructor!

# when we call display then and then it show details of student
s.display()  

