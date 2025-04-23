#q1)
def count_lower_upper(str):
    s= 0
    for i in str:
        if (i.isupper()):
            s+=1
    a =0
    for i in str:
        if(i.islower()):
            a+=1
    return(s,a)
def input_():
    str = input("Enter a string")
    g,h = count_lower_upper(str)
    d = {'lower':g, 'upper': h}
    print(d)
input_()

#q2)
def addval(n):
    s = 0
    v = n
    for i in range(4):
        s = s+n
        n = n*10+v
        print(i, n, s)
    return s

for x in range(4,8):
    print(addval(x))

#q3) 
    def create_array1(x,n):
    I =[]
    for i in range(x):
        I = I +[n]
    return I

x = int(input('How many elements you want to create in array:'))
n = int(input('With what value should I inialize this array:'))
a1 = create_array1(x,n)
print(a1)

#def create_array2(x,y,n):
 #   I= []
  #  for i in range(x):
   #     m = m.append(I)

def create_array3(x,y,z,v):
    I = []
    for i in range(x):
        m = []
        for j in range(y):
            n=[]
            for k in range(z):
                n = n+[v]
            m.append(n)
        I.append(n)
    return I
x = int(input('How many rows you want in array:'))
y = int(input('How many columns you want in array:'))
z = int(input('How many elements you want in array:'))
n = int(input('With what value should I inialize this array:'))
a3 =  create_array3(x,y,z,n)
print(a3)

#q4)
def add(x,y,z,a,b):
    c = x+y+z+a+b
    print("Sum is:", c)
    
def avg(x,y,z,a,b):
    v = (x+y+z+a+b)/5
    print("Average is:", v)

x = int(input("Enter the 1st number:"))
y = int(input("Enter the 2nd number:"))
z = int(input("Enter the 3rd number:"))
a = int(input("Enter the 4th number:"))
b = int(input("Enter the 5th number:"))

add(x,y,z,a,b)
avg(x,y,z,a,b)

#q5)
def pangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    print(alphaset)
    s = s.lower()
    s = set(s)
    return(alphaset <= s)
str = "The quick brown fox jumps over tho lazy dog"
print(str,pangram(str))
str = "Crazy Fredrick bought many vey exquisite opal jewels"
print(str,pangram(str))
str = "Priyam"
print(str, pangram(str))

#q6)
def tuple_in_list(x):
    l =[]
    k = ()
    for i in range(1,x+1):
        k = (i, i*i, i*i*i)
        l.append(k)
    return l
x = int(input("Enter a number:"))
print(tuple_in_list(x))

#q7)
def ispalindrome(x):
    if x==x[::-1]:
        return (True)
    else:
        return(False)
x=input("enter the string:")
print(ispalindrome(x))

#q8)
def convert(s1):
    s=set(s1)
    l=str(s)
    print(l)
    s1="".join(sorted(s))
    return s1
s1=input("enter a string:")
print(convert(s1))

#q9)
def count_alpha_digits(s):
    l=list(s)
    a=0
    n=0
    for i in l:
        if i.isalpha():
            a+=1
        elif i.isdigit():
            n+=1
    return(a,n)

s=input("enter a string:")
a,n=count_alpha_digits(s)
d={'alpha':a,'number':n}
print(d)

#10)
def frequency(s):
    word=s.split()
    l={}
    for i in word:
        i=i.lower()
        if i in l:
            l[i]+=1
        else:
            l[i]=1
    f=sorted(l.items())
    return dict(f)
s=input("enter a string:")
r=frequency(s)
print(r)

#11)
def create_list(l1,l2):
     inter = list(set(l1)&set(l2))
    return inter
l1=[1,2,3,4,5]
l2=[2,5,6,7,8]
r=create(l1,l2)
print(r)

    
    
