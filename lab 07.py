#lab 07

#1
dict1 = {"a": 1,"b": 2}
dict2 = {"c": 3,"d": 4}
dict3 = {"e": 5,"f": 6}
dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)
print("Concatenated dictionary:", dict4)

#2
my_dict = {}
# Check if the dictionary is empty
if not my_dict:
 print("The dictionary is empty.")
else:
 print("The dictionary is not empty.")

#3
employees = [
{"dept_no": 101,"roll_no": 1,"salary": 50000},
{"dept_no": 101,"roll_no": 2,"salary": 60000},
{"dept_no": 102,"roll_no": 3,"salary": 45000},
{"dept_no": 102,"roll_no": 4,"salary": 70000},
{"dept_no": 103,"roll_no": 5,"salary": 55000},
{"dept_no": 103,"roll_no": 6,"salary": 65000}
]

dept_salary = {}

for emp in employees:
 dept_no = emp["dept_no"]
 salary = emp["salary"]
 if dept_no not in dept_salary:
      dept_salary[dept_no] = []
 dept_salary[dept_no].append(salary)
for dept, salaries in dept_salary.items():
 print(f"Department {dept}: Min Salary = {min(salaries)}, Max Salary ={max(salaries)}")

#4
input_string = input("Enter a string: ")
frequency = {}
for char in input_string:
 if char in frequency:
       frequency[char] += 1
 else:
     frequency[char] = 1
print("Character frequencies:", frequency)

#5
prices = {"apple": 50,"banana": 20,"bread": 30,"milk": 40}
quantity = {"apple": 3,"banana": 5,"bread": 2,"milk": 1}
total_bill = 0
for item, qty in quantity.items():
  if item in prices:
      total_bill += prices[item] * qty
print("Total bill:", total_bill)
