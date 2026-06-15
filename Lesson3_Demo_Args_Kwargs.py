def order_fruit(fruit, *args, **kwargs):
    print(f"Ordering {fruit}")
    if fruit == "apple":
        price_unit = 10
        box_per_kg = 1
    elif fruit == "banana":
        price_unit = 5
        box_per_kg = 2
    else:
        price_unit = 2
        box_per_kg = 3
    for arg in args:
        price = args[0] * price_unit
        weight = args[1] * box_per_kg

    for key, value in kwargs.items():
        shipping_cost_perkg = kwargs["shipping_cost"]
        total_cost = price + shipping_cost_perkg  * weight
        shipping_from = kwargs["shipping_from"]
        shipping_to = kwargs["shipping_to"]
        if shipping_to == "NC":
            shipping_travel = "Domestic"
        else:
            shipping_travel = "International"

    return total_cost, shipping_from, shipping_to, shipping_travel, weight



fruit = "apple"
unit_quantity = [10,20]
shipping_details = {    
    "shipping_cost": 10,
    "shipping_from": "NY",
    "shipping_to": "NC"
}

total_cost, shipping_from, shipping_to, shipping_travel, weight = order_fruit(fruit, *unit_quantity, **shipping_details)

print(f"Total cost: {total_cost}")
print(f"Shipping from: {shipping_from}")
print(f"Shipping to: {shipping_to}")
print(f"Shipping travel: {shipping_travel}")    
print(f"Boxes: {weight}")

