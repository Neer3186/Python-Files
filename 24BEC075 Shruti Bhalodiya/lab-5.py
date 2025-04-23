#Lab-5:list

import random

# 1. Replace odd list's 3rd element with even list and flatten
print("\n1️⃣ Create odd/even lists, replace and flatten:")
odd_list = [int(input(f"Enter odd number {i+1}: ")) for i in range(5)]
even_list = [int(input(f"Enter even number {i+1}: ")) for i in range(4)]
print("Original odd list:", odd_list)
print("Even list:", even_list)

odd_list[2] = even_list
print("After replacing 3rd element:", odd_list)

# Flatten
flat_list = []
for x in odd_list:
    if isinstance(x, list):
        flat_list.extend(x)
    else:
        flat_list.append(x)
print("Flattened list:", flat_list)
flat_list.sort()
print("Sorted list:", flat_list)

# 2. Find positions of a number in a random list
print("\n2 Find all occurrences of a number in random list:")
rand_list = [random.randint(1, 10) for _ in range(20)]
print("Random list:", rand_list)
search_num = int(input("Enter number to search for: "))
positions = [i for i, val in enumerate(rand_list) if val == search_num]
print(f"Positions of {search_num}:", positions)

# 3. Remove duplicates from 50 random numbers
print("\n3️Remove duplicates from random list:")
dup_list = [random.randint(1, 30) for _ in range(50)]
print("With duplicates:", dup_list)
unique_list = list(set(dup_list))
print("Without duplicates:", unique_list)

# 4. Separate positive and negative numbers
print("\n4️Separate +ve and -ve numbers from a list:")
mix_list = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
pos_list = [x for x in mix_list if x > 0]
neg_list = [x for x in mix_list if x < 0]
print("Positive numbers:", pos_list)
print("Negative numbers:", neg_list)

# 5. Convert 5 strings to uppercase
print("\n5️Convert strings to uppercase:")
str_list = [input(f"Enter string {i+1}: ") for i in range(5)]
uppercased = [s.upper() for s in str_list]
print("Uppercased strings:", uppercased)

# 6. Convert Fahrenheit to Celsius
print("\n6️Convert Fahrenheit to Celsius:")
f_list = [float(input(f"Enter temperature in Fahrenheit {i+1}: ")) for i in range(5)]
c_list = [round((f - 32) * 5/9, 2) for f in f_list]
print("Celsius temperatures:", c_list)

# 7. Stack (menu-driven)
print("\n7 Stack operations:")
stack = []
def push():
    stack.append(input("Enter value to PUSH: "))
def pop():
    print("Popped:", stack.pop() if stack else "Stack is empty")
def display_stack():
    print("Stack:", stack)

# 8. Queue (menu-driven)
print("\n8️Queue operations:")
queue = []
def enqueue():
    queue.append(input("Enter value to ENQUEUE: "))
def dequeue():
    print("Dequeued:", queue.pop(0) if queue else "Queue is empty")
def display_queue():
    print("Queue:", queue)

# Menu for Stack and Queue
while True:
    print("\nChoose: 1.Push 2.Pop 3.Show Stack 4.Enqueue 5.Dequeue 6.Show Queue 0.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display_stack()
    elif choice == 4:
        enqueue()
    elif choice == 5:
        dequeue()
    elif choice == 6:
        display_queue()
    elif choice == 0:
        break
    else:
        print("Invalid choice!")

# 9. List comprehension for list difference
print("\n9️Create new list from List1 with values not in List2:")
list1 = [int(input(f"Enter value {i+1} for List 1: ")) for i in range(5)]
list2 = [int(input(f"Enter value {i+1} for List 2: ")) for i in range(5)]
diff_list = [x for x in list1 if x not in list2]
print("List 1:", list1)
print("List 2:", list2)
print("Values in List 1 not in List 2:", diff_list)
