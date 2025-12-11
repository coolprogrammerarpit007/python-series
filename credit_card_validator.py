credit_card_number = input("Enter Credit Card Number: ").strip().replace(" ", "")

clear_digit = credit_card_number[-1]
reversed_number = list(reversed(credit_card_number[0:-1]))



# double digits of even index of reversed 
def mul_by_2(numbers):
    double_reversed_digits = []
    for position,number in enumerate(numbers):
        if position % 2 == 0:
            double_reversed_digits.append(int(number) * 2)
            
        else:
            double_reversed_digits.append(int(number))
            
    return double_reversed_digits


result = mul_by_2(reversed_number)


def smooth_numbers(numbers):
    updated_list = []
    
    for number in numbers:
        if int(number) > 9:
            new_number = int(number) - 9
            updated_list.append(new_number)
            
        else:
            updated_list.append(number)
            
    return updated_list

updated_list = smooth_numbers(result)



updated_list.append(int(clear_digit))



total_sum = sum(updated_list)


if total_sum % 10 == 0:
    print("Valid Card")
    
else:
    print("Invalid Card")