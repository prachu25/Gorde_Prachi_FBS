# Multiple Inheritance - Derived class inherits from multiiple Base classes

class Father:
    def father_method(self):
        print("Father method")


class Mother:
    def mother_method(self):
        print("Mother method")


class Child(Father, Mother):
    def child_method(self):
        print("Child method")


obj = Child()

obj.father_method()
obj.mother_method()
obj.child_method()