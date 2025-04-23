#q1
def dict1() :

    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 3, 'd': 4}
    d3 = {'e': 5, 'f': 6}
    d4 = {**d1, **d2, **d3}
    print("Concatenated Dictionary:", d4)

dict1()
#q2
def dict2(input_dict) :
    if not input_dict : 
        return "The dictionary is empty."
    else:
        return "The dictionary is not empty."
    
dic1 = {}
dic2 = {'a': 1, 'b': 2}

print(dict2(dic1)) 
print(dict2(dic2))
#q3
def dict3() :

    employees = {
        101: [
            {"roll_no": 1, "salary": 50000},
            {"roll_no": 2, "salary": 60000},
            {"roll_no": 3, "salary": 70000},
        ],
        102: [
            {"roll_no": 4, "salary": 40000},
            {"roll_no": 5, "salary": 50000},
            {"roll_no": 6, "salary": 45000},
        ],
        103: [
            {"roll_no": 7, "salary": 75000},
            {"roll_no": 8, "salary": 85000},
            {"roll_no": 9, "salary": 90000},
        ]
    }

    def find_min_max_salary(employees):
        department_salaries = {}
        
        for dept_no, employee_list in employees.items():
            salaries = [emp["salary"] for emp in employee_list]
            min_salary = min(salaries)
            max_salary = max(salaries)
            
            department_salaries[dept_no] = {"min_salary": min_salary, "max_salary": max_salary}
        
        return department_salaries

    department_salary_range = find_min_max_salary(employees)

    for dept_no, salary_range in department_salary_range.items():
        print(f"Department {dept_no} - Min Salary: {salary_range['min_salary']}, Max Salary: {salary_range['max_salary']}")

dict3()
#q4
def dict4(input_string) :

    frequency_dict = {}

    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict

str = input("Enter a string: ")
frequency = dict4(str)
print("Character Frequency Dictionary:", frequency)
#q5
def dict5() :

    prices = {
    'apple': 200,     
    'banana': 50,  
    'milk': 60,        
    'bread': 30,     
    'cheese': 150    
    }

    quantities = {
    'apple': 4,      
    'banana': 6,      
    'milk': 2,        
    'bread': 1,        
    'cheese': 1        
    }
    total = 0
    for item in prices:
        if item in quantities:
            total += prices[item] * quantities[item]
    return total

total_bill = dict5()
print(f"Total bill: ₹{total_bill}")
