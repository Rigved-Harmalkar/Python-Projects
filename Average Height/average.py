#For input of heights
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#As we are not using sum and len function we use for loop
total_height = 0 
for height in student_heights:
    total_height+=height
no_of_students = 0
for student in student_heights:
    no_of_students += 1
#total average 
total = total_height/no_of_students
#using round function to remove the recurring.
print(round(total))