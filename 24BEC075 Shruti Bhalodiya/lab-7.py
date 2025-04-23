#Lab-7:Dictonary

# 1. Concatenate three dictionaries
print("\n#1: Concatenate Three Dictionaries")
dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}
dict3 = {'e': 500, 'f': 600}
dict4 = dict1.copy()
dict4.update(dict2)
dict4.update(dict3)
print("Combined dictionary:", dict4)

# 2. Check if dictionary is empty
print("\n#2: Check if Dictionary is Empty")
check_dict = {}
if not check_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

# 3. Department-wise Min and Max Salary
print("\n#3: Department-wise Min & Max Salary")
# Dictionary: {dept_no: [(emp_id, salary), ...]}
company = {
    'D001': [(101, 50000), (102, 55000), (103, 47000)],
    'D002': [(201, 60000), (202, 58000)],
    'D003': [(301, 45000), (302, 49000), (303, 51000)]
}
for dept, records in company.items():
    salaries = [salary for _, salary in records]
    print(f"Department {dept} - Min Salary: {min(salaries)}, Max Salary: {max(salaries)}")

# 4. Character Frequency in String
print("\n#4: Character Frequency in a String")
user_input = input("Enter a string: ")
char_freq = {}
for ch in user_input:
    char_freq[ch] = char_freq.get(ch, 0) + 1
print("Character frequencies:", char_freq)

# 5. Grocery Bill Calculation
print("\n#5: Grocery Billing Using Two Dictionaries")
# First dictionary: item -> price
# Second dictionary: item -> quantity
grocery_prices = {
    'rice': 50,
    'sugar': 40,
    'milk': 30,
    'flour': 25
}
grocery_quantity = {
    'rice': 2,
    'sugar': 1,
    'milk': 3,
    'flour': 4
}
total = 0
for item in grocery_prices:
    item_total = grocery_prices[item] * grocery_quantity.get(item, 0)
    print(f"{item.capitalize()}: {grocery_prices[item]} x {grocery_quantity.get(item, 0)} = {item_total}")
    total += item_total
print("Total Bill:", total)
