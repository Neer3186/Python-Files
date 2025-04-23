def q1():
    l=str(input("enter a sentence:")).split()
    a={x.upper() for x in l}
    print(a)
q1()

import random
def q2():
    a=set()
    while len(a)!=10:
        x=random.randint(15,45)
        a.add(x)
    print(a)
    d=set()
    c=0
    for x in a:
        if x<30:
            c+=1
        if x>35:
            d.add(x)
    a= a - d
    print('the no. of values less than 30:',c)
    print('after deleting the values greater than 35:',a)
q2()

def q3():
    s=set()
    for i in range(5):
        s.add(input("enter the name:"))
    print(s)
    new=input("enter a name to modify")
    if new in s:
        newnm=input("replace i with:")
        s.remove(new)
        s.add(newnm)
    else:
        print(new,"not found")
    print(s.pop(),"is deleted")
    print(s.pop(),"is deleted")
    print("final list:",s)
q3()

def q4():
    s={'ananya','ami','swaroopa','anupama','brinda','brijesh'}
    print(s)
    sa=set()
    sb=set()
    for n in s:
        if n[0]=='a':
            sa.add(n)
        elif n[0]=='b':
            sb.add(n)
    print(sa)
    print(sb)
    sa1={nm for nm in s if nm[0]=='a'}
    sa2={nm for nm in s if nm[0]=='b'}
    print(sa1)
    print(sa2)
q4()

def extra():
    l=[1,2,3,3,2,4]
    print(l)
    s=list(set(l))
    print(s)    
extra()
    
