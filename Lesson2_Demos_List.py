# ### **Steps to be followed:**

# 1. Create a list containing at least 10 elements of different data types (integers, strings, and floats)
# 2. Access and print elements using positive indexing from the list
# 3. Access and print elements using negative indexing from the list
# 4. Perform slicing operations to extract a sublist from the original list
# 5. Append a new element and remove an existing element from the list



my_list = [42,560.75,"Hello",True,34.78,"World",False,200,3.14,"Python"]

print("Length of list:", len(my_list))

for items in my_list:
    print(items)

print("Printing elements using positive index")
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
print(my_list[6])
print(my_list[7])
print(my_list[8])
print(my_list[9])

print("Printing elements using negative index")
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-5])
print(my_list[-6])
print(my_list[-7])
print(my_list[-8])
print(my_list[-9])
print(my_list[-10])


#Slicing operation
print(my_list[0:4:2])
print(my_list[-1:-5:-2])

my_list.append("Validate")
print("List after appending new element:", my_list)

my_list.remove(200)
print("List after removing element:", my_list)

my_list.insert(2,"third element")
print("List after inserting element:", my_list)

print(my_list.count("third element"))

# Sort using string keys so mixed data types can be ordered safely
my_list.sort(key=str)
print("List after sorting:", my_list)

my_list2 = ["new_list1", "new_list2", "new_list3"]

my_list.extend(my_list2)
print("List after extending with another list:", my_list)

my_list3 = my_list + my_list2
print("List after concatenating two lists:", my_list3)

my_list4 = list(my_list), list(my_list2)
print("List after creating a tuple of two lists:", my_list4)