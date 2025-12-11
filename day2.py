# Day 2 Exercises

user_name = input("Enter UserName: ")
user_age = input("Enter UserAge: ")

print(f"User Name is: {user_name} and he is {user_age} years old!")


hourly_wage = input("Please enter your hourly wage: ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
hours_worked = input("How many hours did you work this week? ")
print(hours_worked)


total_wage = float(hours_worked) * float(hourly_wage)
print("Total Payment: ",total_wage)
