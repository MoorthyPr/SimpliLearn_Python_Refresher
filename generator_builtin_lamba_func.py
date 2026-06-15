#generator function

def generate_numbers(n):
    for i in range(n):
        yield i


#lambda function
square = lambda x: x ** 2
even_numbers = lambda x: x % 2 == 0

#Built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

even_nums = list(filter(even_numbers, numbers))
print(even_nums)


gen = generate_numbers(5)
for num in gen:
    print(num)
print(square(5))