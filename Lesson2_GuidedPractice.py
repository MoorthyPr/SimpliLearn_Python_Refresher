#Getting Customer basic info with feedbacks

num_of_customers = int(input("How many customers feedback you want to give :"))

customers_details_dict = {}
customers_details_list = []
customer_details_list_with_category = []
positive_words = {"good", "excellent", "great", "amazing", "professional"}
negative_words = {"bad", "poor", "terrible", "slow", "worst"}

for i in range(num_of_customers):
    customer_details = input("Enter customer details (Name, Age, City,Feedback) separated by comma: ")
    name, age, city, feedback = customer_details.split(",")
    customers_details_dict = {
        "name": name.strip(),
        "age": int(age.strip()),
        "city": city.strip(),
        "feedback": feedback.strip()
    }
    customers_details_list.append(customers_details_dict)
    
# print(customers_details_list)

#Categorizing feedbacks

# for customer in customers_details_list:
#     print(customer)
#     feedback = customer["feedback"].lower()
#     if any(word in feedback for word in positive_words):
#         customer["feedback_category"] = "Positive"
#     elif any(word in feedback for word in negative_words):
#         customer["feedback_category"] = "Negative"
#     else:
#         customer["feedback_category"] = "Neutral"
    
#     customer_details_list_with_category.append(customer)

# print(customer_details_list_with_category)

# print(customers_details_dict)

feedback_dict = {}

for customer in customers_details_list:
    feedback_dict[customer["name"]] = customer["feedback"]
   

for name, feedback in feedback_dict.items():
    feedback_words = set(feedback.lower().split())
    if feedback_words & positive_words:
        feedback_dict[name] = "Positive"
    elif feedback_words & negative_words:
        feedback_dict[name] = "Negative"
    else:
        feedback_dict[name] = "Neutral"

for customer in customers_details_list:
    words_in_feedback = set(customer["feedback"].lower().split())
    if words_in_feedback & positive_words:
        customer["feedback_category"] = "Positive"
    elif words_in_feedback & negative_words:
        customer["feedback_category"] = "Negative"
    else:
        customer["feedback_category"] = "Neutral"

print(feedback_dict)
print(customers_details_list)

positive_set = [customer for customer in customers_details_list if customer["feedback_category"] == "Positive"]
negative_set = [customer for customer in customers_details_list if customer["feedback_category"] == "Negative"]
neutral_set = [customer for customer in customers_details_list if customer["feedback_category"] == "Neutral"]

print("Positive Feedback Customers:", positive_set)
print("Negative Feedback Customers:", negative_set)
print("Neutral Feedback Customers:", neutral_set)
