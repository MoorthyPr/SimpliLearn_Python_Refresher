employee = (
    "John Smith",
    1001,
    "Charlotte",
    "Business Analyst"
)

#Display employee name.
print("Emp Name:", employee[0])

#Check whether employee works in Charlotte.
if 'Charlotte' in employee:
    print("Employee works in Charlotte.")

#Count number of elements in employee tuple.
print("Number of elements in employee tuple:", len(employee))

#Unpack values into variables.
name,emp_id, location, role = employee
print("Name:", name)    

customer = (
    101,
    "David",
    "Savings",
    25000
)

if customer[3] > 20000:
    print(f"Customer {customer[1]} has a high balance of {customer[3]}.")

#Convert to list and add email.

employee_list = list(employee)
employee_list.append("john.smith@example.com")

print(employee_list)
print(set(employee_list))


products = (
    ("Laptop",800),
    ("Monitor",250),
    ("Keyboard",50),
    ("Mouse",25)
)

#Display all product names.
for product in products:
    print("Product Name:", product[0])

#Find the most expensive product.
most_expensive_product = max(products, key=lambda x: x[1])
print("Most expensive product:", most_expensive_product[0], "with price", most_expensive_product[1])