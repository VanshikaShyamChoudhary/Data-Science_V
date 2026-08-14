student={
    "name":"Vanshika",
    "code":"Python",
    "marks":98,
    45.76:87,
    "subjects":{
        "maths":78,
        "english":76.09,
        
         }
   
}
print(list(student.keys()))
print(student.values())
print(student.items())
print(student.get("subjects"))

new_dict={"surname":"Choudhary", "name":"Shyam"}
student.update(new_dict)

print(student)