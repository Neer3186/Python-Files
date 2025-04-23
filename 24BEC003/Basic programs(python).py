#q1)
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
sum=num1+num2
print("sum of two number is:",sum)

#q2)
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
sub=num1-num2
print("sum of two number is:",sub)

#q3)
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
mul=num1*num2
print("sum of two number is:",mul)

#q4)
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
div=num1//num2
print("sum of two number is:",div)

#q5)
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
sum = number1 + number2
sub= number1 number2
mul= number1 * number2
div = number1 / number2
print("Addition is: ", sum)
print("Subtraction is: ", sub)
print("multiplication is: ", mul)
print("Division is: ", div)

#q6)
a = int(input("enter hour to convert into minutes: "))
hour = a*60
print("hence minutes are: ", hour)

#q7)
a = float(input("enter minutes to convert into hours: "))
min = a/60
print("hence hours are: ", min)

#q8)
a = int(input("enter dollar to convert into rupees: "))
rup = a*48
print("hence rupees are: ", rup)

#q9)
a=int(input("enter rupees to convert into dollar: "))
dollar=a/48
print("hence rupees are: ", dollar)

#q10)
a = int(input("enter dollar to convert into pounds: "))
pound = (70/48)*a
print("hence pound are:",pound)

#q11)
a float(input("enter gram to convert into kilogram: "))
kg = a/1000
print("hence kilograms are:", kg)

#q12)
a= float(input("enter kg to convert into gram: "))
g=a*1000
print("hence grams are: ", g)

#q13)

a=float(input("enter the amount of bytes: "))
kb = a/1024
mb = a/(1024*1024)
gb = a/(1024*1024*1024)
print("hence KB, MB, GB are: ", kb, mb, gb)

#q14)

a = float(input("enter celcius to convert into fahrenheit: "))
f = ((9/5)*a) + 32
print("hence fahrenheit are: ", f)

#q15)

a = float(input("enter fahrenheit to convert into celsius: "))
c = 5/9 * (a-32)
print("hence celsius are: ", c)

#q16)

a = float(input("enter amount: "))
i = a/100
print("hence interest: ", i)

#q17)

a = float(input("enter the length of square: "))
area = a*a
peri = 4*a
print("hence area and perimeter of a square are: ', area, peri)

#q18)

a = float(input("enter the length of rectangle: "))
b = float(input("enter the breadth of rectangle: "))
area = a*b
peri = 2*(a+b)
print("hence area and perimeter of a square are: ", area, peri)

#q19)

a = float(input("enter the radius of circle: "))
area = 3.14 * a * a
print("hence area is: ", area)

#q20)

a = float(input("enter the radius of circle: "))
area = 3.14 * a * a
print("hence area is: ", area)

#q21)

a = float(input("enter the gross salary: "))
b = 10/100 * a
c = 3/100 * a
net = a + b - c
print("hence net salary is: ", net)

#q22)

a = float(input("enter the gross sales: "))
net = a - (10/1000)*a
print("hence net sales is: ", net)

#q23)

a = float(input("enter marks for 1st subject: "))
b = float(input("enter marks for 2nd subject: "))
c = float(input("enter marks for 3rd subject: "))
avg = (a + b + c)/3
total = a + b + c
print("hence the average and total are: ", avg, total)

#q24)

a = float(input("enter 1st number: "))
b = float(input("enter 2nd number: "))
print("before swapping: ", a , b)
a,b=b,a
print("after swapping: ", a, b)



