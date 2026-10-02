class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __sub__(self, c):
        return Complex(self.real - c.real, self.imag - c.imag)

    def display(self):
        print(self.real, "+", self.imag, "i")

    def __del__(self):
        print("Object deleted")