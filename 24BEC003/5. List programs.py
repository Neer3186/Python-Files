#Q1)
import random
odd_list = random.sample(range(1, 100, 2), 5)
print(f"Original Odd List: {odd_list}")
even_list = random.sample(range(2, 100, 2), 4)
print(f"Generated Even List: {even_list}")
odd_list[2] = even_list
print(f"Updated List (Nested Even List at index 2): {odd_list}")
flattened_list = []
for item in odd_list:
    if isinstance(item, list):
        flattened_list.extend(item)  
    else:
        flattened_list.append(item)
print(f"Flattened List: {flattened_list}")
flattened_list.sort()
print(f"Sorted Final List: {flattened_list}")

#Q2)
import random
numbers = [random.randint(1, 10) for a in range(20)]
print("Generated List:", numbers)
num = int(input("Enter a number to find its positions: "))
positions = [i for i, val in enumerate(numbers) if val == num]
if positions:
    print(f"{num} found at positions: {positions}")
else:
    print(f"{num} is not in the list.")

#Q3)

import random
numbers = [random.randint(1, 30) for _ in range(50)]
print("Original List (With Duplicates):", numbers)
unique_numbers = list(set(numbers))
print("List After Removing Duplicates:", unique_numbers)


#Q4
import random
numbers = [random.randint(-50, 50) for _ in range(30)]
print("Original List:", numbers)
positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]
print("Positive Numbers List:", positive_numbers)
print("Negative Numbers List:", negative_numbers)

#Q5)

strings = ["hello", "world", "python", "coding", "example"]
uppercase_strings = [s.upper() for s in strings]
print("Original List:", strings)
print("Uppercase List:", uppercase_strings)

#Q6)

fahrenheit_temps = [32, 50, 77, 95, 104]
celsius_temps = [(f - 32) * 5 / 9 for f in fahrenheit_temps]
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Temperatures in Celsius:", celsius_temps)


#Q9)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8, 10]
list3 = [num for num in list1 if num not in list2]
print("First List:", list1)
print("Second List:", list2)
print("Third List (Elements in First List but not in Second):", list3)
