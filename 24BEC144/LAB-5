#1
import random
odd_list = [random.randint(1, 100) * 2 - 1 for _ in range(5)]
print("List of 5 odd integers:", odd_list)
even_list = [random.randint(1, 100) * 2 for _ in range(4)]
print("List of 4 even integers:", even_list)
odd_list[2] = even_list
print("After replacing the third element:", odd_list)
flattened_list = []
for item in odd_list:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)
flattened_list.sort()
print("Sorted flattened list:", flattened_list)

a = [1, 2, 3]
a.extend([4])
a.append([4])

#2
import random
random_list = [random.randint(1, 10) for _ in range(20)]
print("Generated list:", random_list)
num = int(input("Enter a number to find its positions: "))
positions = []
for i in range(len(random_list)):
    if random_list[i] == num:
        positions.append(i)
print(f"Positions of {num} in the list: {positions}")

#3
import random
random_list = [random.randint(1, 30) for _ in range(50)]
print("Original list:", random_list)
i = 0
while i < len(random_list):
    if random_list.count(random_list[i]) > 1:
        random_list.pop(i)
    else:
        i += 1
print("List after removing duplicates:", random_list)

#4
import random
random_list = [random.randint(-50, 50) for _ in range(30)]
print("Generated list:", random_list)
positive_list = [num for num in random_list if num > 0]
negative_list = [num for num in random_list if num < 0]
print("Positive numbers:", positive_list)
print("Negative numbers:", negative_list)

#5
string_list = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", string_list)
uppercase_list = [s.upper() for s in string_list]
print("Uppercase list:", uppercase_list)

#6
fahrenheit_list = [32, 98.6, 212, 77, 104]
celsius_list = [(f - 32) * 5 / 9 for f in fahrenheit_list]
print("Fahrenheit list:", fahrenheit_list)
print("Celsius list:", celsius_list)

#7
stack = []
while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to push: ")
        stack.append(item)
        print(f"{item} pushed to stack.")
    elif choice == 2:
        if stack:
            print(f"{stack.pop()} popped from stack.")
        else:
            print("Stack is empty!")
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

#8
queue = []
while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to enqueue: ")
        queue.append(item)
        print(f"{item} added to queue.")
    elif choice == 2:
        if queue:
            print(f"{queue.pop(0)} removed from queue.")
        else:
            print("Queue is empty!")
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

#9
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [num for num in list1 if num not in list2]
print("List 1:", list1)
print("List 2:", list2)
print("List 3 (numbers in List 1 not in List 2):", list3)

