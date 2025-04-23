#Q1
def countvowel():
    name = input("Enter a string:")
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count+=1
    print('No. of vowels in name:', count)
countvowel()
#Q2
def lower(str):
    str = input('Enter the string:')
    newstr = ' '
    for i in str:
        if 'A' <= i <= 'Z':
            newstr += chr(ord(i)+32)
        else:
            newstr += i
    print(newstr)
lower(str)
def upper(str):
    str = input('Enter the string:')
    newstr = ' '
    for i in str:
        if 'a' <= i <= 'z':
            newstr += chr(ord(i)-32)
        else:
            newstr += i
    print(newstr)
upper(str)
def toggle(str):
    str = input('Enter the string:')
    newstr = ' '
    for i in str:
        if 'a' <= i <= 'z':
            newstr += chr(ord(i)-32)
        else:
            newstr += chr(ord(i)+32)
    print(newstr)
toggle(str)

#Q3
def Compare_str():
    S1 = input("Enter string 1:")
    S2 = input('Enter string 2:')
    if S2 in S1:
        print ('string 2 present in string 1')
    else:
        print('Not present')
Compare_str()

#Q4
def Removestr():
    S1 = input("Enter string 1:")
    S2 = input('Enter string 2:')
    if S2 in S1:
        Sp = S1.replace(S2, '')
        print(Sp)
    else:
        print('Not in')

Removestr()
