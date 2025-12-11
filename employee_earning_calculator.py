employee_name = input("Enter Employee Name: ").strip().title()
hourly_wage = float(input("Enter Employee Hourly Wage: "))
hours_worked = float(input("Enter Employee Weekly hours work: "))

total_wage = hourly_wage * hours_worked

print(f"{employee_name} earned ${total_wage} this week.")