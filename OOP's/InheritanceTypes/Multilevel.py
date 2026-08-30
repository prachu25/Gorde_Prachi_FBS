# Multilevel Inheritance - A one class inherit from another class and another class inhrerit ffrom another class.
class Grandparent:
    def grandparent_method(self):
        print("Grandparent method")


class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")


class Child(Parent):
    def child_method(self):
        print("Child method")


obj = Child()

obj.grandparent_method()
obj.parent_method()
obj.child_method()