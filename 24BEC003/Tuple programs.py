#Q1
Boys = ('b1', 'b2', 'b3', 'b4')
Girls = ['g1', 'g2', 'g3', 'g4']
Girls.append(Boys)
print(Girls)
a = tuple(Girls)
print(a)
C1 = 0
C2 = 0
for i in a:
    if(isinstance(i,tuple)):
        C1 += len(i)
    elif(isinstance(i, str)):
        C2 +=1
print('No. of boys is:', C1)
print('No. of girls:', C2)

#Q2
students = [(3, "Swaroopa", 18), (43, "Vidhi", 19), (59, "Naiyya", 20), (61, "Navya", 12)]
Roll_No = []
Name = []
Ages = []
for i in students:
    Roll_No.append(i[0])
    Name.append(i[1])
    Ages.append(i[2])
print(Roll_No)
print(Name)
print(Ages)

#Q3
import datetime
def q3():
    d1 = (18, 2, 25)
    d2 = (17, 2, 24)
    date1 = datetime.date(d1[2], d1[1], d1[0])
    date2 = datetime.date(d2[2], d2[1], d2[0])
    print(type(date1))
    print(abs(date1-date2))
q3()
#Q4
def q4():
    price = [('Soup', 90), ('Samosa', 20),('Pizza', 100),('Burger', 150)]
    for i in price:
        print(i)
    print(sorted(price))
    import operator
    print(sorted(price, key = operator.itemgetter(1), reverse = True))
q4()
#Q5
def q5():
    L1 = [(), (3,6), (2,8), (), ('Hi',),()]
    L2 = []
    for i in L1:
        if i:
            L2.append(i)
    print(L2)
q5()
#Q6
def q6():
    T1 = ('A', 'B', 'C', 'D')
    T1_list = list(T1)
    T1_list[2] = 2
    T2 = tuple(T1_list)
    print(T2)
q6()
#Q7
def q7():
    t1 = (22,44,66,88)
    L = list(t1)
    L.pop(2)
    print(L)
    t2 = tuple(L)
    print(t2)
q7()


