# #### **Steps to be followed:**

# 1. Create a set with at least seven unique elements, including numbers and strings
# 2. Add a new element to the set and remove an existing one
# 3. Try adding a duplicate element and observe the result
# 4. Perform union, intersection, and difference operations with another set
# 5. Use a set to remove duplicates from a list
# 6. Convert a set into a list and a tuple


my_set = {42, 560.75, "Hello", True, 34.78, "World", False}
print("Original Set:", my_set)

#Adding a new element to the set
my_set.add("Python")

print("Set after adding new element:", my_set)

#Removing an existing element from the set
my_set.remove("Hello")
print("Set after removing an element:", my_set)

my_set.add("Python")
print("Set after adding duplicate element:", my_set)

another_set = {34.78, "World", "Python", "New Element"}
print("Another Set:", another_set)

#Performing union, intersection and difference operations
print("Union of sets:", my_set.union(another_set))
print("Intersection of sets:", my_set.intersection(another_set))
print("Difference of sets:", my_set.difference(another_set))

#Another way of doing the same operations
print("Union of sets:", my_set | another_set)
print("Intersection of sets:", my_set & another_set)
print("Difference of sets:", my_set - another_set)