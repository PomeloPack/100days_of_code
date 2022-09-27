import random

# len 52
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# len 10
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# len 9
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Random PyPassword Generator!")




random_number_letters= int(input("How many letters would you like in your password?\n")) 
random_number_numbers = int(input("How many symbols would you like?\n"))
random_number_symbols = int(input("How many numbers would you like?\n"))


# easy way to create random password generator
# this way choose letter, number and symbol one by one not together random firs will be only letters than numbers and last will be symbols
# example: abc012!#
"""
password = " "

for letter in range(1, random_number_letters + 1):
    password += random.choice(letters)

for number in range(1, random_number_numbers + 1):
    password += random.choice(numbers)

for symbol in range(1, random_number_symbols + 1):
    password += random.choice(symbols)

print(password)
"""

# hard way
# mixing letter, numbers and symbols together 
# example: (456#88))JK/

password_list = []

# random_number_numbers = 4
# our len will be 1 - 4
for letter in range(1, random_number_numbers + 1):
    password_list.append(random.choice(letters))
    

for number in range(1, random_number_numbers + 1):
    password_list.append(random.choice(numbers))

for symbol in range(1, random_number_symbols + 1):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)


final_password = ""
for password in password_list:
  final_password += password

print(f"Your generated password is: {final_password}")











