# Falsely Values 

# Any numeric representation of zero. This includes the integer 0, the float 0.0, and representations of zero in other numeric types.
# The values False and None. We haven't looked at None yet, but None represents the intentional absence of a value.
# Empty sequences and other collections. This includes empty strings, empty tuples, empty lists, and several types we haven't covered at this stage.

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]


numbers = [1, 2, 3, 4]
numbers.append(5)



# print(new_numbers == numbers)
# print(f"New Numbers List Memory Address: {id(new_numbers)}")
# print(f"Numbers List Memory Address: {id(numbers)}")
# print(new_numbers is numbers)


# number = int(input("Enter Number: "))

# if number > 0:
#     print(f"Number {number} is a Positive Number!")
    
# elif number < 0:
#     print(f"Number {number} is a Negative Number.")
    
# else:
#     print("Zero Number")


employee_name = input("Enter Employee Name: ")
employee_weekly_work_hours = int(input("Enter Employee Working Hours: "))
employee_wage = None
Employee_Pay_Hour = 20

if employee_weekly_work_hours <= 40:
    employee_wage = Employee_Pay_Hour * employee_weekly_work_hours
    
elif employee_weekly_work_hours > 40:
    extra_hours = employee_weekly_work_hours - 40
    print("Employee is due some additional Pay: ")
    extra_pay = 1.1 * Employee_Pay_Hour
    employee_wage = Employee_Pay_Hour * (employee_weekly_work_hours - extra_hours) + (extra_hours * extra_pay)
    
else:
    print("Employee On Leave!")
    
    
print("Employee Wage: " + str(employee_wage))