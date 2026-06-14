#Create a function
#Call the function and pass arguments to the function
#Display the results

#Salary calculator function
def salary_calculator(working_hours = 8, hourly_rate = 50):
    salary_for_the_day = working_hours * hourly_rate
    return salary_for_the_day


manager_salary = salary_calculator(8,80)
print(f"Manager Salary for the day: {manager_salary}")
night_shift_employee = salary_calculator(hourly_rate = 55 , working_hours = 9)
print(f"Night Shift Salary for the day: {night_shift_employee}")
regular_employee = salary_calculator()
print(f"Regular Salary for the day: {regular_employee}")

