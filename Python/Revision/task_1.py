# Task 1: Create a Person class

# Attributes: name, age

# Constructor to initialize values

# Method: display_details()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        print(f"{self.name}=name")   
        print(f"{self.age}=age") 

p1=person("Vanshika","21")  
p2=person("Draupadi","25")      

p1.details()
p2.details()
