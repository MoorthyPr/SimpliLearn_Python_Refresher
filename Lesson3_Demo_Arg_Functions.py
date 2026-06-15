#Function for food company to caluclate orders

def calculate_order_total(*orders):
    total_orders = sum(orders)
    number_of_orders = len(orders)
    average_order = total_orders / number_of_orders if number_of_orders > 0 else 0
    highest_order = max(orders) if orders else 0
    lowest_order = min(orders) if orders else 0

    return total_orders, number_of_orders, average_order, highest_order, lowest_order


total, count, average, highest, lowest = calculate_order_total(100, 200, 150, 300)
print(f"Total: {total}, Count: {count}, Average: {average}, Highest: {highest}, Lowest: {lowest}")
