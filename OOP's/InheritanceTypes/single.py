# Single Inheitances -  Derived class inheritance from base class

class Animal:

    def sound(self):
        print('kee kee')


class Dog(Animal):

    def sleep(self):
        print('Dog is slepping..')

    def sound(self):
        super().sound()    # call ANimal's sound()
        print('bark bark..')

obj = Dog()

obj.sleep()
obj.sound()
