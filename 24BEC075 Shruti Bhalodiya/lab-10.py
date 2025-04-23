#Lab-10:File Handling

import csv
import os
import shutil
import pickle

# 1. Write a program to create a CSV file that can be directly opened in MS-Excel
def create_csv_file():
    data = [
        ['RollNo', 'Name', 'Subject1', 'Subject2', 'Subject3'],
        [1, 'riya', 90, 85, 88],
        [2, 'aaryan', 78, 80, 79],
        [3, 'siddhi', 92, 89, 91]
    ]
    
    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("CSV file 'students.csv' created successfully.")

create_csv_file()

# 2. Read the data stored in MS-Excel file (CSV format) and convert it into a dictionary
def read_csv_and_convert_to_dict():
    data_dict = {}
    
    with open('students.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rollno = row['RollNo']
            name = row['Name']
            marks = [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])]
            total = sum(marks)
            data_dict[rollno] = {'Name': name, 'Marks': marks, 'Total': total}
    
    print("Dictionary containing student data:")
    print(data_dict)

read_csv_and_convert_to_dict()

# 3. Accept contact details from the user and create a vCard
def create_vcard():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    
    vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
    """
    
    with open(f"{name}_contact.vcf", 'w') as file:
        file.write(vcard)
    print(f"vCard for {name} created successfully!")

create_vcard()

# 4. Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory
def create_subdirectory_and_copy_file():
    # Create a subdirectory
    os.makedirs("new_directory", exist_ok=True)
    
    # Copy a file from another subdirectory to the newly created subdirectory
    src_file = 'source_directory/example.txt'  # Change with your actual file path
    dest_file = 'new_directory/example.txt'
    
    if os.path.exists(src_file):
        shutil.copy(src_file, dest_file)
        print(f"File copied to 'new_directory/{os.path.basename(src_file)}'.")
    else:
        print("Source file does not exist.")

create_subdirectory_and_copy_file()

# 5. Write a program to copy contents of one file to another while replacing lowercase characters with uppercase
def copy_and_uppercase():
    with open('source.txt', 'r') as file_in:
        content = file_in.read()
        
    content_uppercase = content.upper()
    
    with open('destination.txt', 'w') as file_out:
        file_out.write(content_uppercase)
    
    print("Contents copied and converted to uppercase in 'destination.txt'.")

copy_and_uppercase()

# 6. Write a program that merges lines alternatively from two files and writes to a new file
def merge_lines_alternatively():
    with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('merged_output.txt', 'w') as output_file:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
        
        # Merge alternatively
        merged_lines = []
        for line1, line2 in zip(file1_lines, file2_lines):
            merged_lines.append(line1)
            merged_lines.append(line2)
        
        # Add remaining lines if one file is longer
        longer_lines = file1_lines[len(file2_lines):] if len(file1_lines) > len(file2_lines) else file2_lines[len(file1_lines):]
        merged_lines.extend(longer_lines)
        
        output_file.writelines(merged_lines)
    print("Lines merged into 'merged_output.txt'.")

merge_lines_alternatively()

# 7. Serialize and Deserialize Employee object
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

def serialize_employee():
    emp = Employee(101, 'John Doe', '2022-01-15', 50000)
    with open('employee.pkl', 'wb') as file:
        pickle.dump(emp, file)
    print("Employee data serialized.")

def deserialize_employee():
    with open('employee.pkl', 'rb') as file:
        emp = pickle.load(file)
    print(f"Deserialized Employee Data:\nEmpCode: {emp.empcode}\nName: {emp.empname}\nDOJ: {emp.doj}\nSalary: {emp.salary}")

serialize_employee()
deserialize_employee()

# 8. Delete words ‘a’, ‘the’, ‘an’ in a file and replace with blank space
def delete_words_in_file():
    with open('input.txt', 'r') as file_in:
        content = file_in.read()
    
    words_to_remove = ['a', 'the', 'an']
    for word in words_to_remove:
        content = content.replace(f" {word} ", " ")
    
    with open('output.txt', 'w') as file_out:
        file_out.write(content)
    
    print("Words removed and content saved to 'output.txt'.")

delete_words_in_file()
