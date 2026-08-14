class student:
    def __init__(self,name,course,roll_no,proffesion):
        self.name=name
        self.course=course
        self.roll_no=roll_no
        self.proffesion=proffesion

    def details(self):
        print(f"name:{self.name}") 
        print(f"course:{self.course}") 
        print(f"roll_no:{self.roll_no}") 
        print(f"proffesion:{self.proffesion}")  
 
st1=student("Vanshika","b.tech","110","data scientist\n")
st2=student("Charu","b.tech","0003","data analyst")

st1.details()
st2.details()

