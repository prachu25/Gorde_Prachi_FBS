import pickle

class Emp:

    def __init__(self, emp_nm, age, salary):
        self.emp_nm = emp_nm
        self.age = age
        self.salary = salary

    def display(self):
        print(self.emp_nm, self.age, self.salary)

    def __str__(self):
        return f"{self.emp_nm} {self.age} {self.salary}"


# WRITE FILE

e = Emp("Rohit", 22, 45000)
e2 = Emp("Ishan", 23, 4600)

file = open("emp.txt", "ab")

pickle.dump(e, file)
pickle.dump(e2,file)

file.close()

print("Employee added Successfully...")




# READ FILE

f = open("emp.txt", "rb")

e = pickle.load(f)

print(e)

f.close()