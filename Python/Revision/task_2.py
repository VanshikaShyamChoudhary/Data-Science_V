# Task 2:  Create a Student class
# Inherit from Person
# Additional attributes: student_id, course, marks
# Method: calculate_grade()

# 90–100 → A

# 75–89 → B

# 60–74 → C

# 40–59 → D

# Below 40 → F

# Override display_details() to include student information and grade.

class Student:
    def __init__(self,name,student_id, course, marks):
            self.name=name
            self.student_id=student_id
            self.course=course
            self.marks=marks

    def calculate_grade(self):
          if self.marks>=90:
                print("A")
          elif self.marks>=75:
                print("B")   
          elif self.marks>=60:
                print("C")
          elif self.marks>=40:
                print("D")
          elif self.marks<40:
                print("F")

    def display_details(self):
          print(f"{self.name}=name")
          print(f"{self.student_id}=student_id")
          print(f"{self.course}=course")
          print(f"{self.marks}=marks")

s1=Student("Vanshika","110","B.tech",int(input()))  

s1.display_details()
s1.calculate_grade()

          
                      

                
                  