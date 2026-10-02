class Televison:

    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0


    def take_input(self):

        self.model_number = int(input("Enter model number: "))


        if len(str(self.model_number)) > 4:
            raise ValueError("Model number cannot have more than 4 digits")

        self.screen_size = float(input("Enter screen size: "))

        if self.screen_size < 12 or self.screen_size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")  

        self.price = float(input("Enter price: "))

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")


    def display(self):
        print("\nTelevision Details")
        print("Model Number:", self.model_number)
        print("Screen Size:", self.screen_size)
        print("Price:", self.price)

tv  = Televison()

try:
    tv.take_input()

except ValueError as e:
    print("Error: ", e)

    tv.model_number = 0
    tv.screen_size = 0
    tv.price = 0


tv.display()