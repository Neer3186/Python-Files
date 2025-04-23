#1
students = [("John",), "Alice", ("Mike",), "Emma", ("Raj",), "Priya"]
boys = 0
girls = 0
for student in students:
    if isinstance(student, tuple):
        boys += 1
    else:
        girls += 1
print("Number of boys:", boys)
print("Number of girls:", girls)

#2
students = [(1, "John", 20), (2, "Alice", 19), (3, "Mike", 21)]
roll_no = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]
print("Roll No.:", roll_no)
print("Names:", names)
print("Ages:", ages)

#3
d1 = (18, 2, 2025)
d2 = (18, 2, 2024)

if d1 > d2:
    d1, d2 = d2, d1

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day1, month1, year1 = d1
day2, month2, year2 = d2
days = 0

while (day1, month1, year1) != (day2, month2, year2):
    day1 += 1
    days += 1
    if month1 == 2:
        max_days = 29 if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0) else 28
    else:
        max_days = days_in_months[month1 - 1]
    if day1 > max_days:
        day1 = 1
        month1 += 1
        if month1 > 12:
            month1 = 1
            year1 += 1

print("Days between dates:", days)

#4 Create a list of tuples containing a food item and its
food_prices = [("Pizza", 250), ("Burger", 150), ("Pasta", 200), ("Fries", 100)]
sorted_food = sorted(food_prices, key=lambda x: x[1], reverse=True)
print("Sorted food items by price (desc):", sorted_food)

#5
tuples_list = [(), (1, 2), (), (3, 4), (), (5, 6)]
filtered_list = [t for t in tuples_list if t]
print("List after removing empty tuples:", filtered_list)

#6
my_tuple = (1, 2, 3)
temp_list = list(my_tuple)
temp_list[1] = 99
my_tuple = tuple(temp_list)
print("Modified tuple:", my_tuple)

#7
my_tuple = (1, 2, 3, 4, 5)
temp_list = list(my_tuple)
del temp_list[2]
my_tuple = tuple(temp_list)
print("Tuple after deleting an element:", my_tuple)
