#lab-1:write python programs for the following (simple programs)


# 1. Add two numbers
a, b = 5, 3
print("Addition:", a + b)

# 2. Subtract two numbers
print("Subtraction:", a - b)

# 3. Multiply two numbers
print("Multiplication:", a * b)

# 4. Divide two numbers
print("Division:", a / b)

# 5. All operations
print("Add:", a + b, "Sub:", a - b, "Mul:", a * b, "Div:", a / b)

# 6. Convert hours into minutes
hours = 2
print("Minutes:", hours * 60)

# 7. Convert minutes into hours
minutes = 180
print("Hours:", minutes / 60)

# 8. Convert dollars into Rs. (1$ = 48 Rs.)
dollars = 10
print("Rs:", dollars * 48)

# 9. Convert Rs. into dollars (1$ = 48 Rs.)
rupees = 480
print("Dollars:", rupees / 48)

# 10. Convert dollars into pounds
# 1$ = 48 Rs, 1 pound = 70 Rs
print("Pounds:", (dollars * 48) / 70)

# 11. Convert grams into kg
grams = 1000
print("Kg:", grams / 1000)

# 12. Convert kgs into grams
kg = 5
print("Grams:", kg * 1000)

# 13. Convert bytes into KB, MB, GB
bytes_val = 10485760  # 10 MB
print("KB:", bytes_val / 1024)
print("MB:", bytes_val / (1024**2))
print("GB:", bytes_val / (1024**3))

# 14. Celsius to Fahrenheit
c = 37
f = (9/5) * c + 32
print("Fahrenheit:", f)

# 15. Fahrenheit to Celsius
f = 98.6
c = (5/9) * (f - 32)
print("Celsius:", c)

# 16. Calculate interest
P, R, N = 1000, 5, 2
I = (P * R * N) / 100
print("Interest:", I)

# 17. Square area and perimeter
L = 4
print("Square Area:", L**2, "Perimeter:", 4 * L)

# 18. Rectangle area and perimeter
L, B = 5, 3
print("Rectangle Area:", L * B, "Perimeter:", 2 * (L + B))

# 19. Area of a circle
R = 7
print("Circle Area:", (22/7) * R * R)

# 20. Area of a triangle
H, L = 6, 4
print("Triangle Area:", (H * L) / 2)

# 21. Net Salary
gross_salary = 50000
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print("Net Salary:", net_salary)

# 22. Net Sales
gross_sales = 20000
discount = 0.10 * gross_sales
net_sales = gross_sales - discount
print("Net Sales:", net_sales)

# 23. Average of 3 subjects
sub1, sub2, sub3 = 85, 90, 80
total = sub1 + sub2 + sub3
average = total / 3
print("Total:", total, "Average:", average)

# 24. Swap two values
x, y = 10, 20
x, y = y, x
print("Swapped Values: x =", x, "y =", y)
