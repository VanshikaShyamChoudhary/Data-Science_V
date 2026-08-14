# Abstraction
class car:
    def __init__(self):
        car.acc=False
        car.clutch=False
        car.brk=False

    def start(self):
        self.clutch=True
        self.acc=False
        print("car started.....")


car1=car() 
car1.start()           