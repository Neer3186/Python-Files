def ls2():
    n1=int(input("enter the first no.:"))
    n2=int(input("enter the second no.:"))
    if(n1<n2):
        print(n2,"the largest number")
    elif(n1==n2):
        print("both numbers are equal")
    else:
        print(n1,"the largest number")
ls2()
ls2()
def ls3():
    n1=int(input("enter the first no.:"))
    n2=int(input("enter the second no.:"))
    n3=int(input("enter the third no.:"))
    if((n2>n3)and (n2>n3)):
        print(n2,"the largest number")
    elif(n1>n2):
        print(n1,"the largest number")
    elif(n3>n1):
        print(n3,"the largest number")
    else:
        print("all numbers are equal")
ls3()
ls3()
ls3()
def q3():
    n1=int(input("enter the no.:"))
    if((n1%2)==0):
        print(n1,"is even number")
    else:
        print(n1,"is odd number")
q3()

def q4():
    n1=int(input("enter the no.:"))
    
    if((n1%10)==0):
        print(n1,"is divisible by 10")
    else:
        print(n1,"is not divisible by 10")
q4()
def q5():
    n1=int(input("enter the age:"))
    if(n1>18):
        print("major")
    else:
        print("minor")
q5()
q5()
def q6():
    n1=int(input("enter a number:"))
    n2=str(n1)
    n3=len(n2)
    print("the number of digits in the number:",n3)
q6()
q6()
def q7():
    n1=int(input("enter the year:"))
    if((n1%4)==0):
        print(n1,"is a leap year")
    else:
        print(n1,"is not a leap year")
q7()
q7()
def q8():
    n1=int(input("enter the first angle:"))
    n2=int(input("enter the second angle:"))
    n3=int(input("enter the third angle:"))
    s=n1+n2+n3
    if(s==180):
        print("it is a triangle")
    else:
        print("it is not a triangle")
q8()
q8()
def q9():
    n1=int(input("enter a number:"))
    if(n1<0):
        n2=-(n1)
        print("the absolute value:",n2)
    else:
        print("the absolute value of number is:",n1)
q9()
q9()
def q12():
    import math
x,y= map(float, input("Enter circle center (x y): ").split())
r=int(input("enter the radius of the circle:"))
x1,y1= map(float, input("Enter circle center (x y): ").split())
z=math.sqrt((x-x1)**2+(y-y1)**2)
if (z==pow(r,2)):
    print("the point is under circle")
else:
    print("the point is not in the circle")
q12()
def q13():
    num_words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen"
    }
    x=int(input("enter a number (0-19):"))
    print(num_words[x])
q13()



