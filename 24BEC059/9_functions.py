#q1
def lower_upper(x):
     s=0
     a=0
     for i in x:
          if (i.isupper()):
               s+=1
          if(i.islower()):
               a+=1
    return(s,a)
def input_():
     c=input("enter the string:")
     g,h=lower_upper(x)
     print(['upper':g,'lower':h])
input_()
#q3
def create_array(x,y,z,v):
    l=[]
    for i in range(z):
        m=[]
        for j in range(y):
            n=[]
            for k in range(x):
                l=l+[v]
            m.append(n)
        l.append(m)
    return(l)
def input_():
    x=int(input("x="))
    y=int(input("y="))
    z=int(input("z="))
    v=int(input("value="))
    a=create_array(x,y,z,v)
    print(a)
input_()

#q4
def sum_(a,b,c,d,e):
     f=a+b+c+d+e
     return(f)
def avg_(a,b,c,d,e):
     f=(a+b+c+c+d+e)//5
     return(f)
def inp():
     a=int(input("enter 1st numbers:"))
     b=int(input("enter 2nd numbers:"))
     c=int(input("enter 3rd numbers:"))
     d=int(input("enter 4th numbers:"))
     e=int(input("enter 5th numbers:"))
     g=sum_(a,b,c,d,e)
     h=avg_(a,b,c,d,e)
     print("the sum of 5 numbers:",g)
     print("the avg of 5 number:",h)
inp()
 
#q5
def pangram(s):
    a=set('abcdefghijklmnopqrstuvwxyz ')
    print(a)
    s=s.lower()
    s=set(s)
    return(a<=s)


s="a b c d e f ghijklmnopqrstuvwxyz"
print(pangram(s))

#q6
def tuple_in_list(x):
    l=[]
    k=()
    for i in range(1,x+1):
        k=(i,i*i,i*i*i)
        l.append(k)
    return l
x=int(input("enter a number:"))
print(tuple_in_list(x))

#q7
def ispalindrome(x):
    if x==x[::-1]:
        return (True)
    else:
        return(False)
x=input("enter the string:")
print(ispalindrome(x))

#q8
def convert(s1):
    s=set(s1)
    l=str(s)
    print(l)
    s1="".join(sorted(s))
    return s1
s1=input("enter a string:")
print(convert(s1))

#q9
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

#10
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

#11
def create_list(l1,l2):
     inter = list(set(l1)&set(l2))
    return inter
l1=[1,2,3,4,5]
l2=[2,5,6,7,8]
r=create(l1,l2)
print(r)
     
