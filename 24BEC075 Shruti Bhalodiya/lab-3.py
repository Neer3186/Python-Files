#lab-3:Strings in python

# 1. Count vowels in a string
def count_vowels():
    s = input("Enter a string: ")
    s = s.lower()
    vowels = 'aeiou'
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)

# 2. Convert to lowercase, uppercase, toggle case without built-in methods
def to_lower(s):
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

def to_upper(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result

def toggle_case(s):
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

def case_conversion():
    s = input("Enter a string for case conversion: ")
    print("Lowercase:", to_lower(s))
    print("Uppercase:", to_upper(s))
    print("Toggle case:", toggle_case(s))

# 3. Check if one string is in another
def string_in_string():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string to search in first: ")
    if str2 in str1:
        print(f"'{str2}' is found in '{str1}'")
    else:
        print(f"'{str2}' is NOT found in '{str1}'")

# 4. Remove one string from another, if present
def remove_substring():
    onestring = input("Enter the original string: ")
    removestring = input("Enter the substring to remove: ")
    result = ""
    i = 0
    while i < len(onestring):
        if onestring[i:i+len(removestring)] == removestring:
            i += len(removestring)
        else:
            result += onestring[i]
            i += 1
    print("Final string after removal:", result)

# Call the functions
count_vowels()
case_conversion()
string_in_string()
remove_substring()
