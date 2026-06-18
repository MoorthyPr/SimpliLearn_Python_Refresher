# Customer names - List of all customer names

# from pprint import pprint


customer_names = [
    "John Smith", "Emma Johnson", "Michael Brown", "Sophia Davis",
    "William Wilson", "Olivia Taylor", "James Anderson", "Ava Thomas",
    "Benjamin Martin", "Isabella White", "Lucas Harris", "Mia Clark",
    "Henry Lewis", "Charlotte Walker", "Alexander Hall", "Amelia Allen",
    "Daniel Young", "Harper King", "Matthew Scott", "Evelyn Green"
]

# Customer Orders - Name, Product, Price, Category
customer_orders = [
    ("John Smith", "Laptop", 1200.00, "Electronics"),
    ("John Smith", "Wireless Mouse", 25.99, "Electronics"),
    ("Emma Johnson", "Running Shoes", 10.50, "Sports"),
    ("Emma Johnson", "Yoga Mat", 20.00, "Sports"),
    ("Michael Brown", "Coffee Maker", 23.99, "Home Appliances"),
    ("Michael Brown", "Blender", 22.75, "Home Appliances"),
    ("Sophia Davis", "Smartphone", 899.99, "Electronics"),
    ("Sophia Davis", "Phone Case", 15.99, "Accessories"),
    ("William Wilson", "Office Chair", 150.00, "Furniture"),
    ("William Wilson", "Desk Lamp", 35.00, "Furniture"),
    ("Olivia Taylor", "Tablet", 499.99, "Electronics"),
    ("Olivia Taylor", "Stylus Pen", 29.99, "Electronics"),
    ("James Anderson", "Basketball", 24.99, "Sports"),
    ("James Anderson", "Sports Bag", 39.99, "Sports"),
    ("Ava Thomas", "Cookware Set", 120.00, "Kitchen"),
    ("Ava Thomas", "Knife Set", 45.00, "Kitchen"),
    ("Benjamin Martin", "Gaming Console", 499.00, "Electronics"),
    ("Benjamin Martin", "Video Game", 59.99, "Entertainment"),
    ("Isabella White", "Bookshelf", 180.00, "Furniture"),
    ("Isabella White", "Novel Collection", 75.00, "Books"),
    ("Lucas Harris", "Smart Watch", 199.99, "Electronics"),
    ("Lucas Harris", "Watch Strap", 19.99, "Accessories"),
    ("Mia Clark", "Dress", 89.99, "Fashion"),
    ("Mia Clark", "Handbag", 129.99, "Fashion"),
    ("Henry Lewis", "Headphones", 149.99, "Electronics"),
    ("Henry Lewis", "Bluetooth Speaker", 79.99, "Electronics"),
    ("Charlotte Walker", "Dining Table", 450.00, "Furniture"),
    ("Charlotte Walker", "Table Runner", 25.00, "Home Decor"),
    ("Alexander Hall", "Monitor", 299.99, "Electronics"),
    ("Alexander Hall", "Keyboard", 49.99, "Electronics"),
    ("Amelia Allen", "Air Fryer", 99.99, "Kitchen"),
    ("Amelia Allen", "Recipe Book", 18.99, "Books"),
    ("Daniel Young", "Tennis Racket", 120.00, "Sports"),
    ("Daniel Young", "Tennis Balls", 12.99, "Sports"),
    ("Harper King", "Sofa", 799.99, "Furniture"),
    ("Harper King", "Cushion Set", 49.99, "Home Decor"),
    ("Matthew Scott", "Printer", 199.99, "Electronics"),
    ("Matthew Scott", "Ink Cartridge", 34.99, "Office Supplies"),
    ("Evelyn Green", "Winter Jacket", 159.99, "Fashion"),
    ("Evelyn Green", "Scarf", 24.99, "Fashion"),
    ("Sophia Davis", "Water", 15.99, "Groceries"),
    ("William Wilson", "Water", 150.00, "Groceries"),
]


# Storing product information for each customer in a dictionary

customer_products = {}
customer_total_insights = {}
customer_total_spent = {}
product_categories = set()
product_categories_unique_list = []

for customer in customer_names:
    product_list = []
    customer_insights = []
    total_spent = 0
    for order in customer_orders:
        if order[0].lower() == customer.lower():
            product_list.append(order[1])
            total_spent += order[2]
                
    customer_products[customer] = product_list
    customer_insights.append(total_spent)
    if total_spent > 100:
        customer_insights.append("high-value buyer")
    elif total_spent > 50 and total_spent <= 100:
        customer_insights.append("medium-value buyer")
    else:
        customer_insights.append("low-value buyer")
    customer_total_insights[customer] = customer_insights
    customer_total_spent[customer] = total_spent


#Creating unique set of product categories and copy to unique categories list
for order in customer_orders:
    product_categories.add(order[3])

product_categories_unique_list = list(product_categories)


# Storing set of products for each category in a dictionary
category_products = {}
for order in customer_orders:
    category = order[3]
    product = order[1]
    if category not in category_products:
        category_products[category] = set()
    category_products[category].add(product)


# Generating business insights
product_revenue_dict = {}
for product in product_categories_unique_list:
    total_revenue_per_product = 0
    for order in customer_orders:
        if order[3] == product:
            total_revenue_per_product += order[2]
    product_revenue_dict[product] = total_revenue_per_product

# Unique product set from the customer orders
unique_products = set()
for order in customer_orders:
    unique_products.add(order[1])   



#Sort the customer total insights in descending order
sorted_customer_total_insights = sorted(customer_total_insights.items(), key=lambda x: x[1][0], reverse=True)




#Use a list comprehension to find all customers who purchased electronics
customers_purchased_electronics = [order[0] for order in customer_orders if order[3] == "Electronics"]











            



