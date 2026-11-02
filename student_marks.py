print("STUDENT MARKS CALCULATOR")

name = input("Enter student name: ")

m1 = int(input("Enter Maths marks: "))
m2 = int(input("Enter Science marks: "))
m3 = int(input("Enter English marks: "))
m4 = int(input("Enter Computer marks: "))

total = m1 + m2 + m3 + m4
percentage = total / 4

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")

print("Result Completed")
