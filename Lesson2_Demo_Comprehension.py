# ### **Steps to be followed:**

# 1. List Comprehension: Create a list of squares for numbers 1 to 10 using list comprehension
# 2. Filtering with List Comprehension: Extract only even numbers from a given list using a condition
# 3. Dictionary Comprehension: Generate a dictionary where keys are numbers 1 to 5, and values are their squares
# 4. Conditional Dictionary Comprehension: Filter a dictionary to keep only keys with even values
# 5. Set Comprehension: Create a set that stores unique vowels from a given string
# 6. Convert List to Set using Comprehension: Remove duplicates from a list by converting it into a set using comprehension



#Creating a list of squares for numbers 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print("Squares of numbers 1 to 10:", squares)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = [x for x in my_list if x % 2 == 0]
print("Even numbers from the list:", even_numbers_list)

#Creating a dictionary where keys are numbers 1 to 5, and values are their squares
squares_dict = {x: x**2 for x in range(1, 6)}
print("Dictionary of squares:", squares_dict)

my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
even_values_dict = {k: v for k, v in my_dict.items() if v % 2 == 0}
print("Dictionary with even values:", even_values_dict)

my_string = "Hello World"
vowels_set = {char for char in my_string if char.lower() in 'aeiou'}
print("Unique vowels in the string:", vowels_set)

my_list_dup = [1, 2, 2, 3, 4, 4, 5]
unique_set = {x for x in my_list_dup}
print("Set with duplicates removed:", unique_set)
