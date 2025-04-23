#lab 02

#1
a = 10
b = 5
if a > b:
 print("Largest:", a)
 print("Smallest:", b)
else:
 print("Largest:", b)
 print("Smallest:", a)

#2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = num1
smallest = num1
if num2 > largest:
  largest = num2
if num3 > largest:
 largest = num3
if num2 < smallest:
 smallest = num2
if num3 < smallest:
 smallest = num3
print(f"Largest: {largest}, Smallest: {smallest}")

#3
num = 7
if num % 2 == 0:
 print("Even")
else:
 print("Odd")

#4
num = 50
if num % 10 == 0:
 print("Divisible by 10")
else:
 print("Not divisible by 10")

#5
age = 17
if age < 18:
 print("Minor")
else:
 print("Major")

#6
num = input("Enter a number: ")
print(f"Number of digits in {num} is {len(num)}")

#7
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print("Leap Year")
else:
 print("Not a Leap Year")

#8
angle1 = int(input("Enter Angle 1: "))
angle2 = int(input("Enter Angle 2: "))
angle3 = int(input("Enter Angle 3: "))
if angle1 + angle2 + angle3 == 180:
 print("Valid Triangle")
else:
 print("Invalid Triangle")

#9
num = -10
if num < 0:
 print("Absolute Value:", -num)
else:
 print("Absolute Value:", num)

#10
length = 6
breadth = 4
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
 print("Area is greater")
else:
 print("Perimeter is greater")

#11
x1, y1 = 1, 2
x2, y2 = 3, 4
x3, y3 = 5, 6
area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
if area == 0:
 print("Points lie on the same line")
else:
 print("Points do not lie on the same line")

#12
import math
h, k, r = 0, 0, 5
x, y = 3, 4 
distance = math.sqrt(math.pow(x - h, 2) + math.pow(y - k, 2))
if distance < r:
 print("Inside the Circle")
elif distance == r:
 print("On the Circle")
else:
 print("Outside the Circle")

#13
num = 7
if num == 0:
 print("zero")
elif num == 1:
 print("one")
elif num == 2:
 print("two")
elif num == 3:
 print("three")
elif num == 4:
 print("four")
elif num == 5:
 print("five")
elif num == 6:
 print("six")
elif num == 7:
 print("seven")
elif num == 8:
 print("eight")
elif num == 9:
 print("nine")
elif num == 10:
 print("ten")
elif num == 11:
 print("eleven")
elif num == 12:
 print("twelve")
elif num == 13:
 print("thirteen")
elif num == 14:
 print("fourteen")
elif num == 15:
 print("fifteen")
elif num == 16:
 print("sixteen")
elif num == 17:
 print("seventeen")
elif num == 18:
 print("eighteen")
elif num == 19:
 print("nineteen")
else:
 print("invalid input")


 #14

def get_grade(marks):
    if marks == "Absent":
        return "NA"
    marks = int(marks)
    if marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    elif marks <= 79:
        return "A+"
    else:
        return "O"

marks = []
subjects = ["Math", "Science", "English"]
fail = False
total = 0

for subject in subjects:
    mark = input(f"Enter marks for {subject} (type 'Absent' if student was absent): ")
    if mark.lower() == "absent":
        marks.append("Absent")
        fail = True
    else:
        mark = int(mark)
        marks.append(mark)
        total += mark
        if mark <= 39:
            fail = True

print("\nSubject-wise Grades:")
for i in range(3):
    print(f"{subjects[i]}: {marks[i]} => Grade: {get_grade(marks[i])}")

if "Absent" not in marks:
    average = total / 3
    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")
else:
    print("\nTotal and average not calculated due to absence.")

if fail:
    print("Result: FAIL")
else:
    print("Result: PASS")

