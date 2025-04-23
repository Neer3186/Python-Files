#Q1
def list():
    Lst = ['good', 'evening']
    print(Lst)
    s = set()
    s = {i.upper() for i in Lst}
    print(s)
list()
#Q2
import random
def set2():
    s = set()
    while len(s) != 10:
        x = random.randint(15, 45)
        s.add(x)
    print(s)
    d = set()
    c = 0
    for x in s:
        if x<30:
            c+=1
        if x>35:
            d.add(x)
            s = s-d
            print("No. of elements <30", c)
            print("After deleting the values>35", d)
set2()

#Q3
def set3():
    s = set()
    for i in range(4):
        s.add(input("Enter a name:"))
    print(s)
    nm = input("Enter a name to modify:")
    if nm in s:
        newnm = input("Replace it with:")
        s.remove(nm)
        s.add(newnm)
    else:
        print(nm, "not found")
    print(s.pop(), "is deleted")
    print(s.pop(), "is deleted")
    print("The Final List:", s)
set3()
#Q4

def set4():
    s = {'ananya', 'anushka', 'ami', 'vidhi', 'bhavan', 'bhavani'}
    sa = set()
    sb = set()
    for nm in s:
        if nm[0] == 'a':
            sa.add(nm)
        elif nm[0] == 'b':
            sb.add(nm)
    print (sa)
    print(sb)
set4()

#Q5
def set5():
    l = [1, 2, 3, 1, 5, 6, 5]
    s = set(l)
    print(s)
    lst = list(s)

            










    
        






    
    


    
                  
            
