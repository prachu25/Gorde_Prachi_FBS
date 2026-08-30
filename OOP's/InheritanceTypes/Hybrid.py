# Hybrid Inheritance - A combination of Two or More Types of inheritance.

class A:
    def method_a(self):
        print("A method")


class B(A):
    def method_b(self):
        print("B method")


class C(A):
    def method_c(self):
        print("C method")


class D(B, C):
    def method_d(self):
        print("D method")


obj = D()

obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()