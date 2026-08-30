class Car:

    def __init__(self, brand, model, price):

        self.brand = brand
        self.model = model
        self.price = price

        print("Hey, I am Car Constructor!")

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    

    def getModel(self):
        return self.model

    def setModel(self,model):
        self.model = model


    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    

    def display(self):
        print("\n----- CAR Details -----")
        print(f"Brand : {self.getBrand()}")
        print(f"Model : {self.getModel()}")
        print(f"Price : {self.getPrice()}")


# object Creation
c1 = Car("BMW","X5",9000000 )
c2 = Car("Mahindra", "Thar", 1500000)

c2.setBrand('Porchee')


c1.display()

c2.display()


