class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        # self.percentage=str((self.phy+self.chem+self.maths)/3)+"%"

    @property
    def percentage(self):
        return str ((self.phy+self.chem+self.maths)/3)+"%"

    
    # def calcPercent(self):
    #     self.percentage=str((self.phy+self.chem+self.maths)/3)+"%"

      
s1=Student(85,97,87)
print(s1.percentage) 
# print(s1.phy)
# s1.calcPercent()
s1.phy=56
print(s1.percentage)       