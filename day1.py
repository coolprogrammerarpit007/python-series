# print((4-5)*(5+3)/2) # -4 ->O/p
# print(1/11+4-3/2) # 2.590000


# Exercise


person_age = input("Enter your Age: ")
print(f"Person is {person_age} age years old!")


number_of_years = int(input("Enter Number Of Years: "))
number_of_months = number_of_years * 12
number_of_weeks = number_of_years * 52
number_of_days = number_of_years * 365

print("**************** YEARLY Calculator *************")
print(f"Months in {number_of_years} Years are: {number_of_months}")
print(f"Weeks in {number_of_years} Years are: {number_of_weeks}")
print(f"Days in {number_of_years} Years are: {number_of_days}")


PI = 3.14
circle_radius = float(input("Enter Circle Radius: "))
area_of_circle = PI * circle_radius ** 2
print(f"Area of Circle: {area_of_circle}")