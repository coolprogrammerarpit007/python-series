employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

avg_hourly_wage = 0

for employee in employees:
    emp_wage = employee[1] * employee[2]
    avg_hourly_wage += employee[2]
    print(f"Employee {employee[0]} earns ${emp_wage} at the end of week after working about {employee[1]} hours with daily hourly pay of ${employee[2]}.")
    
avg_hourly_wage = avg_hourly_wage/len(employees)

for employee in employees:
    if employee[2] > avg_hourly_wage:
        print(f"Employee {employee[0]} is earning ${employee[2]} which is more then Average daily Pay of ${avg_hourly_wage}")