cities = [
    "Charlotte",
    "Atlanta",
    "Charlotte",
    "Dallas",
    "Atlanta",
    "Austin"
]

#Removing duplicates
unique_cities= set(cities)
print(unique_cities)

#Add "Houston"
unique_cities.add("Houston")
print(unique_cities)

#Check if "Austin" exists.
if 'Austin' in unique_cities:
    print("Austin exists in the set of unique cities.")

#Count unique cities.

print("Number of unique cities:", len(unique_cities))


customer1 = {"Checking", "Savings", "Credit Card"}
customer2 = {"Savings", "Mortgage", "Credit Card"}


#Find common products used by either customer

common_products = customer1.intersection(customer2)
print("Products used by both customers:", common_products)


#Find all products used by both customers
all_products = customer1.union(customer2)
print("All products used by either customer:", all_products)


#Find products only customer1 owns.
customer1_only = customer1.difference(customer2)
print("Products only customer1 owns:", customer1_only)

#Find products only customer2 owns.
customer2_only = customer2.difference(customer1)
print("Products only customer2 owns:", customer2_only)  


team_a = {"Python", "SQL", "Spark"}
team_b = {"Spark", "AWS", "Databricks"}

#Find combined skills

combined_skills = team_a.union(team_b)
print("Combined skills of both teams:", combined_skills)

common_skills = team_a.intersection(team_b)
print("Common skills between both teams:", common_skills)

unique_skills_team_a = team_a.difference(team_b)
print("Skills unique to Team A:", unique_skills_team_a)

unique_skills_team_b = team_b.difference(team_a)
print("Skills unique to Team B:", unique_skills_team_b)

#Find Skills Requiring Training
skills_requiring_training = team_a.symmetric_difference(team_b)
print("Skills requiring training for both teams:", skills_requiring_training)


transactions = [
    1001,1002,1003,1002,1004,
    1005,1001,1006
]

for trans in transactions:
    print(trans)


new_transaction_set = {trans+1 for trans in transactions}
print(new_transaction_set)