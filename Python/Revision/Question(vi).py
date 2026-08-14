# Parent Class
class Animal:
    def sound(self):
        print("Animals make different sounds")

# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof")

# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow")

# Child Class 3
class Cow(Animal):
    def sound(self):
        print("Cow moos: Moo Moo")

# Objects
d = Dog()
c = Cat()
cw = Cow()

# Polymorphism
d.sound()
c.sound()
cw.sound()