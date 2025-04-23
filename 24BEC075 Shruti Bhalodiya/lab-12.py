#Lab-12:Classes and Objects

# 1. Complex Number Operations
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


print("1. Complex Number Operations:")
r1 = int(input("Enter real part of first complex number: "))
i1 = int(input("Enter imaginary part of first complex number: "))
r2 = int(input("Enter real part of second complex number: "))
i2 = int(input("Enter imaginary part of second complex number: "))
c1 = Complex(r1, i1)
c2 = Complex(r2, i2)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)

# 2. Matrix Class
class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def add(self, other):
        result = [[self.mat[i][j] + other.mat[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def multiply(self, other):
        result = [[sum(self.mat[i][k] * other.mat[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.mat[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def display(self):
        for row in self.mat:
            print(row)

print("\n2. Matrix Operations:")
print("Enter 3x3 Matrix A:")
A = [[int(input(f"A[{i}][{j}]: ")) for j in range(3)] for i in range(3)]
print("Enter 3x3 Matrix B:")
B = [[int(input(f"B[{i}][{j}]: ")) for j in range(3)] for i in range(3)]
matA = Matrix(A)
matB = Matrix(B)
print("Matrix Addition:")
matA.add(matB).display()
print("Matrix Multiplication:")
matA.multiply(matB).display()
print("Transpose of Matrix A:")
matA.transpose().display()

# 3. Solid Class
class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.data = kwargs

    def calculate(self):
        if self.shape == "cube":
            s = self.data["side"]
            return 6 * s**2, s**3
        elif self.shape == "sphere":
            r = self.data["radius"]
            return 4 * 3.14159 * r**2, (4/3) * 3.14159 * r**3
        return 0, 0

print("\n3. Solid Area & Volume:")
shape = input("Enter solid (cube/sphere): ").lower()
if shape == "cube":
    side = float(input("Enter side length: "))
    solid = Solid("cube", side=side)
else:
    radius = float(input("Enter radius: "))
    solid = Solid("sphere", radius=radius)
area, volume = solid.calculate()
print("Surface Area:", area, "Volume:", volume)

# 4. Shape Area & Perimeter
class Shape:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.data = kwargs

    def calculate(self):
        if self.shape == "square":
            s = self.data["side"]
            return s**2, 4 * s
        elif self.shape == "circle":
            r = self.data["radius"]
            return 3.14159 * r**2, 2 * 3.14159 * r
        return 0, 0

print("\n4. Shape Area & Perimeter:")
shape = input("Enter shape (square/circle): ").lower()
if shape == "square":
    side = float(input("Enter side: "))
    shapeObj = Shape("square", side=side)
else:
    radius = float(input("Enter radius: "))
    shapeObj = Shape("circle", radius=radius)
area, peri = shapeObj.calculate()
print("Area:", area, "Perimeter:", peri)

# 5. Time Class
class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def add(self, other):
        total_m = self.m + other.m
        h = self.h + other.h + total_m // 60
        m = total_m % 60
        return Time(h, m)

    def __str__(self):
        return f"{self.h}h:{self.m}m"

print("\n5. Time Addition:")
h1 = int(input("Enter hours of first time: "))
m1 = int(input("Enter minutes of first time: "))
h2 = int(input("Enter hours of second time: "))
m2 = int(input("Enter minutes of second time: "))
t1 = Time(h1, m1)
t2 = Time(h2, m2)
print("Total Time:", t1.add(t2))

# 6. Date Comparison
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def __eq__(self, other):
        return self.d == other.d and self.m == other.m and self.y == other.y

print("\n6. Date Comparison:")
d1 = Date(int(input("Enter day of Date1: ")), int(input("Month: ")), int(input("Year: ")))
d2 = Date(int(input("Enter day of Date2: ")), int(input("Month: ")), int(input("Year: ")))
print("Dates are equal?" , d1 == d2)

# 7. Weather Parameters
class Weather:
    def __init__(self, params):
        self.params = params

    def __contains__(self, item):
        return item in self.params

print("\n7. Weather Class:")
params = input("Enter weather parameters separated by comma: ").split(",")
weather = Weather(params)
check = input("Enter parameter to check: ")
print(f"{check} in weather data?", check in weather)

# 8. Custom String Class
class MyString:
    def __init__(self, val):
        self.value = val

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        return ''.join(ch.lower() if 'A' <= ch <= 'Z' else ch for ch in self.value)

    def toUpper(self):
        return ''.join(ch.upper() if 'a' <= ch <= 'z' else ch for ch in self.value)

print("\n8. Custom String Operations:")
s1 = MyString(input("Enter first string: "))
s2 = MyString(input("Enter second string: "))
s1 += s2
print("Concatenated:", s1.value)
print("To Upper:", s1.toUpper())
print("To Lower:", s1.toLower())
