#q1
a=input("entre a word:")
vowels="aeiouAEIOU"
vowel_count=0
for char in a:
    if char in vowels:
        vowel_count+=1
print(f"the number of vowels in string is:{vowel_count}")
#q2
def lower_case(s):
    re=""
    for char in s:
        if'A'<=char<='Z':
            re+=chr(ord(char)+32)
        else:
            re+=char
    print(re)
def upper_case(r):
    re=""
    for char in r:
        if'a'<=char<='z':
            re+=chr(ord(char)-32)
        else:
            re+=char
    print(re)
def toggle_case(c):
    re=""
    for char in c:
        if'a'<=char<='z':
            re+=chr(ord(char)-32)
        else:
            re+=chr(ord(char)+32)
    print(re)
y=input("enter a word:")
lower_case(y)
upper_case(y)
toggle_case(y)
#q3
def compare_string():
    s1=input("enter a string:")
    s2=input("enter another string:")
    print(s2 in s1)
compare_string()
#q4
def remove():
    s1=input("enter the string:")
    s2=input("enter the another string:")
    if s2 in s1:
        sp=s1.find(s2)
        s1=s1[:sp]+s1[sp:len(s2):]
    print(s1)
remove()
def loop():
    for i in range(65,91):
        print(chr(i),end=" ")
    for i in range(97,123):
        print(chr(i),end=" ")

loop()
def multiple():
    n=int(input("enter the number:"))
    for i in range(1,11):
        print(i,"*",n,"=",(n*i))
multiple()


 
