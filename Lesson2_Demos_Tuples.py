# ### **Steps to be followed:**

# 1. Create a tuple with at least eight elements, including numbers and strings
# 2. Access elements from the tuple using both positive and negative indexing
# 3. Extract a sub-tuple using slicing operations
# 4. Try modifying an element in the tuple and observe the result
# 5. Perform tuple unpacking and assign values to individual variables
# 6. Use the count() and index() methods to analyze elements in a tuple
# 7. Convert a tuple into a list, modify it, and then convert it back into a tuple


my_tuple = (42, 560.75, "Hello", True, 34.78, "World", False, 200)

print("Tuple:", my_tuple)
print("Length of tuple: ",len(my_tuple))

#Accessing elements using positive indexing 
print("Accessing elements using positive indexing:")
print(my_tuple[0])
print(my_tuple[1])

#Accessing elements using negative indexing
print("Accessing elements using negative indexing:")
print(my_tuple[-1])
print(my_tuple[-2])
print(my_tuple[-3])


#slicing operation
print("Slicing operation:")
print(my_tuple[0:4:1])
print(my_tuple[-1:-5:-1])

#Trying to modify an element in the tuple
try:
    my_tuple[0] = 100
except TypeError as e:
    print("Error:", e)

var1, var2, var3, var4, var5, var6, var7, var8 = my_tuple
print("Unpacked tuple variables:")
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
print(var7)
print(var8)

print("Count of 'Hello' in tuple:", my_tuple.count("Hello"))    
print("Index of 'Hello' in tuple:", my_tuple.index("Hello"))
print("printing all elements in the tuple using a loop:")
for item in my_tuple:
    print(item)

#Converting tuple to list, modifying it, and converting back to tuple
my_list = list(my_tuple)
my_list[0] = 100
my_tuple = tuple(my_list)
print("Modified tuple:", my_tuple)