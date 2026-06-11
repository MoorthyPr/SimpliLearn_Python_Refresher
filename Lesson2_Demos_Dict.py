# ### **Steps to be followed:**

# 1. Create a dictionary with at least five key-value pairs, representing a student’s details (e.g., name, age, course, marks)
# 2. Access and print values using keys
# 3. Modify an existing value in the dictionary
# 4. Add a new key-value pair and remove an existing key
# 5. Retrieve all keys, values, and key-value pairs using dictionary methods
# 6. Use the get() method to access a key that may or may not exist



student_dict = {
    "name": "Moorthy",
    "age": 40,
    "course": "Computer Science",
    "marks": 95
}

print("Student Dictionary:", student_dict)
#Accessing values using keys
print("Accessing values using keys:")
print("Name: ", student_dict["name"])
print("Age: ", student_dict["age"])
print("Course: ", student_dict["course"])
print("Marks: ", student_dict["marks"])

#Accesing a key using loop
print("Accessing keys using a loop:")
for key in student_dict:
    print(student_dict[key])

#Accesing values using loop
print("Accessing values using loop:")
for value in student_dict.values():
    print(value)

#Accesing key-value pairs using loop
print("Accessing key-value pairs using loop:")
for key,value in student_dict.items():
    print(f"{key}: {value}")

#Modifying an existing value in the dictionary
student_dict["marks"] = 98
print("Dictionary after modifying marks:", student_dict)

#Adding a new key-value pair
student_dict["email"] = "moorthy@example.com"
print("Dictionary after adding email:", student_dict)

#Removing an existing key
del student_dict["email"]
print("Dictionary after removing email:", student_dict)

#Use get() method to access a key that may or may not exist
print("Using get() method to access a key that may not exist:")
print("Name: ", student_dict.get("name"))
print("Email: ", student_dict.get("email", "Email not found"))

#User set method to add a new key-value pair
student_dict.setdefault("email", "moorthy@example.com")
print("Dictionary after setting default email:", student_dict)

multiplication_table = {}
for i in range(1,6):
    row = []
    for j in range(1,11):
        row.append(i * j)
    multiplication_table[i] = row

print("Multiplication Table:")
for i, row in multiplication_table.items():
    print(f"{i}: {row}")
    