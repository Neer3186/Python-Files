#Lab-8:Sets

import random

# 1. Convert words to uppercase and store in a set
print("\n#1: Convert Words to Uppercase and Store in Set")
word_list = ['apple', 'banana', 'grape', 'orange', 'mango']
upper_set = {word.upper() for word in word_list}
print("Original list:", word_list)
print("Set with uppercase words:", upper_set)

# 2. Random numbers in a set and filter by conditions
print("\n#2: Set of Random Numbers with Conditions")
random_set = {random.randint(15, 45) for _ in range(10)}
print("Original set:", random_set)
less_than_30 = {x for x in random_set if x < 30}
print("Count of numbers less than 30:", len(less_than_30))
random_set = {x for x in random_set if x <= 35}
print("Set after deleting numbers > 35:", random_set)

# 3. Add, modify, and delete from a set
print("\n#3: Add, Modify, Delete Names in a Set")
name_set = set()
# Adding 5 names
for i in range(5):
    name = input(f"Enter name {i+1} to add: ")
    name_set.add(name)

print("Set after adding 5 names:", name_set)

# Modify a name (by removing old and adding new)
name_to_modify = input("Enter the name you want to modify: ")
if name_to_modify in name_set:
    new_name = input("Enter the new name: ")
    name_set.remove(name_to_modify)
    name_set.add(new_name)
    print("Set after modifying name:", name_set)
else:
    print("Name not found in set.")

# Delete 2 names
for i in range(2):
    del_name = input(f"Enter name {i+1} to delete: ")
    name_set.discard(del_name)  # discard avoids error if name not found
print("Set after deletions:", name_set)

# 4. Separate names into two sets by starting letter
print("\n#4: Separate Names by First Letter (A or B)")
name_set = {'Anita', 'Bharat', 'Amit', 'Bhavna', 'Ajay', 'Bobby'}
set_A = {name for name in name_set if name.startswith('A')}
set_B = {name for name in name_set if name.startswith('B')}
print("Original Set:", name_set)
print("Names starting with A:", set_A)
print("Names starting with B:", set_B)
