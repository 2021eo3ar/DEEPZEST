science = float(input("Enter the marks fo science: "))
Maths = float(input("Enter the marks of Maths: "))
Physics = float(input("Enter the marks of Physics: "))
Chemistry = float(input("Enter the marks of Physic Chemistry: "))

average = (science+Maths+Physics+Chemistry)/4
print(f'The final grade of student is {average}')
if average>33.0:
 print("Status: Pass")
else:
 print("Status:Fail")
