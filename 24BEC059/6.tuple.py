def q1():
    b=('b1','b2','b3')
    g=['g1','g2','g3']
    g.append(b)
    print(g)
    countb=0
    countg=0
    for i in g:
        if(isinstance(i,tuple)):
            countb+=len(i)
        elif(isinstance(i,str)):
            countg+=1
    print("the no. of boys in class is:",countb)
    print("the no. of girls in class is:",countg)
q1()
def q2():
    l=[(1,'s1',18),(2,'s2',19),(3,'s3',17)]
    roll=[]
    name=[]
    age=[]
    for i in l:
        roll.append(i[0])
        name.append(i[1])
        age.append(i[2])
    print(roll)
    print(name)
    print(age)
q2()
import datetime
def q3():
    d1=(12,7,25)
    d2=(13,8,25)
    d1_obj= datetime.date(d1[2],d1[1],d1[0])
    d2_obj= datetime.date(d2[2],d2[1],d2[0])
    print(type(d1))
    print(abs(d1_obj-d2_obj))
    
q3()
def q4():
    food_items=[("f1",100),("f2",210),("f3",132)]
    for i in food_items:
        print(i)
        import operator
    sorted(food_items,key=operator.itemgetter(1),reverse= True)
    print(food_items)
q4()
def q5():
    l1=[(),(3,4),(5,7,3,9),('h1',0),()]
    l2=[]
    for i in l1:
        if i:
            l2.append(i)
    print(l2)
q5()
def q6():
    t1=("a","b","c","d")
    t1_l=list(t1)
    t1_l[3]=3
    t2=tuple(t1_l)
    print(t2)
q6()
def q7():
    t1=(4,5,6,7,8)
    l=list(t1)
    l.pop(4)
    print(l)
    t2=tuple(l)
    print(t2)
q7()

