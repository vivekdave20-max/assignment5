#Task 1:Create a Dictionary of Student Marks
students= {"Alice" :85, "Carry":86 ,"Jonson":87}
name=input("enter the student's name:\t")

if name in students:
    print(f"{name}'s marks:",students[name])
else:
    print("student not found.")