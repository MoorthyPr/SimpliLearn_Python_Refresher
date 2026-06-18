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
    ("Sophia Davis", "Story Book", 15.99, "Books"),
    ("William Wilson", "Non-Fiction Book", 150.00, "Books")
]


class Customer:

    '''The __init__ method initializes a Customer instance with customer data:

        customer_names
            a list of all customer names to be analyzed
        customer_orders
            a tuple list containing (name, product, price, category) for each order'''

    def __init__(self,customer_names,customer_orders):
        self.customer_names = customer_names
        self.customer_orders = customer_orders


    
    '''The build_customer_insights method analyzes each customer in self.customer_names and builds three insight structures:

        customer_products
            maps each customer to a list of products they purchased
        customer_total_spent
            maps each customer to their total spending across all orders
        customer_total_insights
            maps each customer to a two-item list:
                total spent
                buyer classification'''


    def build_customer_insights(self):
        customer_total_insights = {}
        customer_total_spent = {}
        customer_products = {}

        for customer in self.customer_names:
            product_list = []
            customer_insights = []
            total_spent = 0
            for order in self.customer_orders:
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

        sorted_customer_total_insights = sorted(customer_total_insights.items(), key=lambda x: x[1][0], reverse=True)

        return customer_total_insights, customer_total_spent, customer_products, sorted_customer_total_insights
    

    '''The build_customer_insights method analyzes each customer in self.customer_names and builds three insight structures:

        customer_products
            maps each customer to a list of products they purchased
        customer_total_spent
            maps each customer to their total spending across all orders
        customer_total_insights
            maps each customer to a two-item list:
                total spent
                buyer classification (high/medium/low-value)
        sorted_customer_total_insights
            sorted version of customer_total_insights by total spent in descending order'''


    def display_customer_insights(self):
        customer_total_insights, customer_total_spent, customer_products , sorted_customer_total_insights = self.build_customer_insights()

        print("============================================================")
        print("**********************Customer Insights*********************")
        print("============================================================")
        for customer, insights in customer_total_insights.items():
            print(f"Customer: {customer}, Total Spent: ${insights[0]}, Customer Type: {insights[1]}, Products Purchased: {customer_products[customer]}")
         
        print("=============================================================")
        print("***************Total Spent at Customer level*****************")
        print("=============================================================")
        for customer, spent in customer_total_spent.items():
            print(f"Total spent by {customer}: ${spent}")

        print("=============================================================")
        print("**********Products Purchased by Each Customer****************")
        print("=============================================================")
        for customer, products in customer_products.items():
            print(f"Products purchased by {customer}: {products}")

        print("=============================================================") 
        print("**********Top 3 Customer Insights****************************")
        print("=============================================================")
        top_3_spent_customers = sorted_customer_total_insights[:3]
        for customer, insights in top_3_spent_customers:
            print(f"Customer: {customer}, Total Spent: ${insights[0]}, Customer Type: {insights[1]}")
  
        print("\n")
        print("*"*100)


    '''The build_product_insights method organizes and categorizes all products:

        product_categories_unique_list
            a list of all unique product categories
        product_categories
            a set of unique category names
        category_products
            a dictionary mapping each category to a set of products in that category
        unique_products
            a set of all unique product names across all orders'''


    def build_product_insights(self):
    
    
        product_categories = set()
        product_categories_unique_list = []
        category_products = {}

        unique_products = set()
   

        for order in customer_orders:
            product_categories.add(order[3].lower())
            category = order[3]
            product = order[1]
            unique_products.add(order[1].lower()) 
            if category not in category_products:
                category_products[category] = set()
            category_products[category].add(product)

        product_categories_unique_list = list(product_categories)

        return product_categories_unique_list,product_categories,category_products,unique_products
    


    '''The display_product_insights method displays product organization with formatted sections:

    unique categories section
        lists all distinct product categories
    products by category section
        shows products grouped under each category
    all unique products section
        displays complete list of all unique products'''
    
    def display_product_insights(self):
        product_categories_unique_list, product_categories, category_products, unique_products = self.build_product_insights()

        print("=============================================================")
        print("******************Unique Product Categories******************")
        print("=============================================================")
        for category in product_categories_unique_list:
            print(f"Category: {category.capitalize()}")

        print("=============================================================")
        print("******************Products in Each Category******************")
        print("=============================================================")
        for category, products in category_products.items():
            print(f"Category: {category.capitalize()}")
            for product in products:
                print(f" - {product.capitalize()}")
                
        print("=============================================================")
        print("******************Unique Products******************")
        print("=============================================================")
        for product in unique_products:
            print(f" - {product.capitalize()}")

        print("\n")
        print("*"*100)


    '''The build_business_insights method calculates revenue metrics by product category:

    product_revenue_dict
        a dictionary mapping each product category to its total revenue
        calculated by summing all order prices for that category'''

    def build_business_insights(self):
        product_revenue_dict = {}
        product_categories_unique_list = self.build_product_insights()[0]
        for product in product_categories_unique_list:
            total_revenue_per_product = 0
            for order in customer_orders:
                if order[3].lower() == product:
                    total_revenue_per_product += order[2]
            product_revenue_dict[product.capitalize()] = total_revenue_per_product

        return product_revenue_dict


    '''The display_business_insights method displays revenue analysis:

    product revenue section
        shows total revenue generated for each product category'''
    
    def display_business_insights(self):
        product_revenue_dict = self.build_business_insights()
        print(f"Total revenue by product category: {product_revenue_dict}")
        print("=============================================================")
        print("******************Product Revenue Insights*******************")
        print("=============================================================")
        for product, revenue in product_revenue_dict.items():
            print(f"Product Category: {product}, Revenue: ${revenue}")

        print("\n")
        print("*"*100)


    '''The find_customers_by_item method searches and retrieves customer information for a specific product:

    search_item
        user input for the product name to search
    customers
        a list of customer names who purchased the specified item
    category
        the product category of the searched item
    customer_category_tuple
        combines customers and their category information'''
    
    def find_customers_by_item(self):
        product_categories_unique_list, product_categories, category_products, unique_products = self.build_product_insights()

        unique_products_list = list(unique_products)

        search_item = input("Enter the item you want to search for: ").lower()
        # print(f"Searching for {search_item}")
        # print(f"Unique products list: {unique_products_list}")
        if search_item not in unique_products_list:
            print("Item not found.")
            return
        customers = [order[0] for order in customer_orders if order[1].lower() == search_item]
        if len(customers) == 0:
            print(f"No customers found for {search_item}.")
        else:
            print(f"Customers who purchased {search_item}: {customers}")

        #Create a tuple of customer names based on the category
        category = [order[3] for order in customer_orders if order[1].lower() == search_item]
        customer_category_tuple = tuple(customers + category)

        print("\n")
        print("*"*100)


    '''The find_unique_customers_combo_items method finds common customers between two products:

    search_item1, search_item2
        two product names entered by user (comma-separated)
    category1_set, category2_set
        sets of customers who purchased each product
    common_customers
        the intersection of both sets (customers who bought both items)'''

    def find_unique_customers_combo_items(self):

        product_categories_unique_list, product_categories, category_products, unique_products = self.build_product_insights()

        unique_products_category_list = list(product_categories_unique_list)

        search_item1, search_item2 = input("Enter 2 Product categories you want to search for (comma-separated) and get the common customers: ").split(",")

        if search_item1.lower() not in unique_products_category_list or search_item2.lower() not in unique_products_category_list:
            print("One or both items not found.")
            return
        else:
            if search_item1.lower() == search_item2.lower():
                print("Please enter two different items.")
                return
            else:
                category1_set = set([order[0] for order in customer_orders if order[3].lower() == search_item1.lower()])
                # print(f"Customers for {search_item1}: {category1_set}")
                category2_set = set([order[0] for order in customer_orders if order[3].lower() == search_item2.lower()])
                # print(f"Customers for {search_item2}: {category2_set}")
                common_customers = category1_set & category2_set
                
                if len(common_customers) == 0:
                    print(f"No matching customers found for {search_item1} and {search_item2}.")
                else:
                    print(f"Customers who bought in product category {search_item1} and {search_item2}: {common_customers}")
        print("\n")
        print("*"*100)

    '''The find_all_customers_combo_items method retrieves all customers who purchased either of two products:

    search_item1, search_item2
        two product names entered by user (comma-separated)
    category1_set, category2_set
        sets of customers who purchased each product
    all_customers
        the union of both sets (customers who bought either item)'''

    def find_all_customers_combo_items(self):

        product_categories_unique_list, product_categories, category_products, unique_products = self.build_product_insights()

        unique_products_category_list = list(product_categories_unique_list)

        search_item1, search_item2 = input("Enter 2 Product categories you want to search for (comma-separated) and get all the customers: ").split(",")

        if search_item1.lower() not in unique_products_category_list or search_item2.lower() not in unique_products_category_list:
            print("One or both items not found.")
            return
        else:
            if search_item1.lower() == search_item2.lower():
                print("Please enter two different items.")
                return
            else:
                category1_set = set([order[0] for order in customer_orders if order[3].lower() == search_item1.lower()])
                # print(f"Customers for {search_item1}: {category1_set}")
                category2_set = set([order[0] for order in customer_orders if order[3].lower() == search_item2.lower()])
                # print(f"Customers for {search_item2}: {category2_set}")
                all_customers = category1_set | category2_set
                if len(all_customers) == 0:
                    print(f"No customers found for {search_item1} and {search_item2}.")
                else:
                    print(f"All of customers who bought products from {search_item1} and {search_item2}: {all_customers}")

        print("\n")
        print("*"*100)


c1 = Customer(customer_names, customer_orders)

run_application = True

while run_application == True:
    
    print("****************************************************************************************************************************")
    print("===================================Welcome to the Customer Orders Insights Application======================================")
    print("****************************************************************************************************************************")

    # print(f"\nDataset used: {customer_orders}")

    print("\nPlease select an option:")

    print("1. Find customers by item")
    print("2. Find unique customers for two product categories")
    print("3. Find all customers for two product categories")
    print("4. Display business insights")
    print("5. Display customer insights")
    print("6. Display product insights")
    print("7. Exit")

    customer_choice = input("Enter your choice (1-7): ")

    if customer_choice == "1":
        c1.find_customers_by_item()
    elif customer_choice == "2":
        c1.find_unique_customers_combo_items()
    elif customer_choice == "3":
        c1.find_all_customers_combo_items()
    elif customer_choice == "4":
        c1.display_business_insights()
    elif customer_choice == "5":
        c1.display_customer_insights()
    elif customer_choice == "6":
        c1.display_product_insights()
    elif customer_choice == "7":
        print("Exiting the application.")
        run_application = False
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")









            



