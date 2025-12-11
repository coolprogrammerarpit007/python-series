# import random

# secret_number = random.randint(1,50)

# user_choice = int(input("Enter Number: "))
# total_guesses = 5


# while total_guesses > 0:
#     if user_choice != secret_number and total_guesses > 0:
#         print("Sorry, Wrong choice!!")
#         total_guesses -= 1
#         print(f"You have {total_guesses} guesses remaining!")
#         user_choice = int(input("Enter Number: "))
        
#     else:
#         total_guesses -= 1
#         print(f"Congrats on guessing correct Number: {secret_number} with {total_guesses} chances remaining...")
#         break
    
# else:
#     print(f"Sorry, Your all chances are exhausted better luck next time!")
#     print(f"Secret Number Was: {secret_number}")
        
        
        
# for char in "Python":
#     if char == 'o':
#         continue
#     print(f"Character: {char}")


# check Prime Numbers

# input_number = int(input("Enter Number: "))

# for num in range(2,input_number):
#     if input_number % num == 0:
#         print(f"Number {input_number} is not a prime number as it is divisible by {num}")
#         break
    
# else:
#     print(f"{input_number} is a Prime Number!")