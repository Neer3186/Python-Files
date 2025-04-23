#1
inputstring = input("Enter a string: ")
string = inputstring.lower()
count = 0
for char in string:
    if char in "aeiou":
        count += 1
print(f"The number of vowels in '{inputstring}' is {count}.")


#2
def to_lowercase(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)
        else:
            result += ch
    return result

def to_uppercase(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += ch
    return result

def toggle_case(s):
    result = ""
    for ch in s:
        ascii_val = ord(ch)
        if 65 <= ascii_val <= 90:
            result += chr(ascii_val + 32)
        elif 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += ch
    return result

text = "Hello, WoRLd! 123"
print("Original:", text)
print("Lowercase:", to_lowercase(text))
print("Uppercase:", to_uppercase(text))
print("Toggle case:", toggle_case(text))

#3
str1 = input("Enter String 1: ")
str2 = input("Enter String 2: ")
if str2 in str1:
    print("String 2 is present inside String 1")
else:
    print("String 2 is not present inside String 1")

#4
main = input("Enter the main string: ")
remove = input("Enter the string which needs to be removed: ")
answer = main.replace(remove, '')
print(answer)
