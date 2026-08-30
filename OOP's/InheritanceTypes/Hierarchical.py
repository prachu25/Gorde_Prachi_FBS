# Hierachical Inheritance = Mukltiple Dervied class inherit from One Base class

class Parent:
    def show(self):
        print("Parent method")


class Child1(Parent):
    def method1(self):
        print("Child1 method")


class Child2(Parent):
    def method2(self):
        print("Child2 method")


obj1 = Child1()
obj2 = Child2()

obj1.show()
obj1.method1()

obj2.show()
obj2.method2()