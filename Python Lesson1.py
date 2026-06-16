# print("Hello World")
# #Get 2 number from user 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(f"{a} > {b} :", a > b)
# print(f"{a} < {b} :", a < b)
# print(f"{a} >= {b} :", a >= b)
# print(f"{a} <= {b} :", a <= b)
# print(f"{a} == {b} :", a == b)
# print(f"{a} != {b} :", a != b)


# positive_words = {"good", "excellent", "great", "amazing", "professional"}


# if positive_words in "I am good at programming":
#     print("The word 'good' is in the set of positive words.")


continue_example = []


for num in range(1,10):
    if num == 5:
        continue
    continue_example.append(num)
print(continue_example)