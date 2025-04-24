#Q-1
def prime_factors(n, i=2):
    if n < 2:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i + 1)

print("Prime factors of 84:", prime_factors(84))

#Q-2
def to_binary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return to_binary(n // 2) + str(n % 2)

print("Binary of 18:", to_binary(18))

#Q-3 
def count_vowels(s):
    if not s:
        return 0
    return (1 if s[0].lower() in 'aeiou' else 0) + count_vowels(s[1:])

print("Vowel count:", count_vowels("Functional Programming Rocks"))

#Q-4
def reverse_list(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + reverse_list(lst[:-1])

print("Reversed list:", reverse_list([1, 2, 3, 4, 5]))

#Q-5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print("3^4 =", power(3, 4))

#Q-6
def sanitize_list(lst):
    if not lst:
        return []
    head = 0 if lst[0] < 0 else lst[0]
    return [head] + sanitize_list(lst[1:])

print("Sanitized list:", sanitize_list([-1, 5, -3, 7, 0, -2]))

#Q-7
def average_list(lst):
    def helper(lst, total=0, count=0):
        if not lst:
            return total / count if count > 0 else 0
        return helper(lst[1:], total + lst[0], count + 1)
    return helper(lst)

print("Average:", average_list([10, 20, 30, 40, 50]))

#Q-8
def string_length(s):
    if s == '':
        return 0
    return 1 + string_length(s[1:])

print("Length of string:", string_length("Recursion"))
