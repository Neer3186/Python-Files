#Lab-6:Tuples

from datetime import date

# 1. Count boys and girls (boys as tuple)
print("\n#1: Count boys and girls in a mixed list")
people = [("Aman", "Rohan"), "Priya", "Sneha", ("Raj", "Karan"), "Anita"]
boys = sum(1 for p in people if isinstance(p, tuple))
girls = sum(1 for p in people if not isinstance(p, tuple))
print("Number of boys groups (tuples):", boys)
print("Number of girls (strings):", girls)

# 2. Split student info from tuple list
print("\n#2: Split roll no., name and age from list of tuples")
students = [(1, "Anil", 20), (2, "Sunita", 21), (3, "Raj", 19)]
roll_nos = [s[0] for s in students]
names = [s[1] for s in students]
ages = [s[2] for s in students]
print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)

# 3. Days between two date tuples
print("\n#3: Days between two date tuples")
date1 = (12, 4, 2025)
date2 = (22, 4, 2025)
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])
print("Days between:", abs((d2 - d1).days))

# 4. Sort food items by price
print("\n#4: Sort food item tuples by price (descending)")
menu = [("Burger", 99), ("Pizza", 250), ("Pasta", 180), ("Fries", 80)]
sorted_menu = sorted(menu, key=lambda x: x[1], reverse=True)
print("Sorted Menu:", sorted_menu)

# 5. Remove empty tuples
print("\n#5: Remove empty tuples from list")
tuples_list = [(), (1, 2), (), (3,), (4, 5, 6), ()]
cleaned_list = [t for t in tuples_list if t]
print("List after removing empty tuples:", cleaned_list)

# 6. Modify an element of a tuple
print("\n#6: Modify an element of a tuple")
tup = (10, 20, 30)
temp = list(tup)
temp[1] = 99
tup = tuple(temp)
print("Modified tuple:", tup)

# 7. Delete an element of a tuple
print("\n#7: Delete an element of a tuple")
tup = (1, 2, 3, 4)
temp = list(tup)
del temp[2]  # deleting the third element (index 2)
tup = tuple(temp)
print("Tuple after deletion:", tup)


