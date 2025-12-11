# first_name,last_name = input("Enter Name: ").strip().split(' ')
# print(f"First Name: {first_name}")
# print(f"Last Name: {last_name}")

numbers = [1, 2, 3, 4, 5]
# print()
# number_string = '|'.join(list(map(lambda num: str(num),numbers)))
# print(number_string)

# quotes = [
#     "'What a waste my life would be without all the beautiful mistakes I've made.'",
#     "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
#     "'The very essence of romance is uncertainty.'",
#     "'We are not here to do what has already been done.'"
#  ]


# for quote in quotes:
#     print(quote[1:-1])



input_string = input("Enter Your Text: ").strip()
total_characters = len(input_string)

str_to_lists = input_string.split(' ')
word_count = len(str_to_lists)

print(f"Input String: {input_string} has {total_characters} total characters with {word_count} words in it.")