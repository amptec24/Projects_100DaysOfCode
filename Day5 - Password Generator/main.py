#Password Generator Project - Written by Allen Clarke
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

# Generating the letters for the password
letter_value = ""
for letter in range(0, nr_letters):
  letter_index = random.randint(0, len(letters) - 1)
  letter_value += letters[letter_index]
# Generating the symbols for the password
symbol_value = ""
for symbol in range(0, nr_symbols):
  symbol_index = random.randint(0, len(symbols) - 1)
  symbol_value += symbols[symbol_index]
# Generating the symbols for the password
number_value = ""
for number in range(0, nr_numbers):
  number_index = random.randint(0, len(numbers) - 1)
  number_value += numbers[number_index]
 
print('\nHere is "Easy"password in order requested\n>>  ' + letter_value + symbol_value + number_value)


# ************************************************************************************************************
#Hard Level - Order of characters randomised:

password_holder = []
letter_value = ""
symbol_value = ""
number_value = ""

# Generating the letters for the password
letter_value = ""
for letter in range(0, nr_letters):
  letter_index = random.randint(0, len(letters) - 1)
  letter_value += letters[letter_index]
  
# Generating the symbols for the password
symbol_value = ""
for symbol in range(0, nr_symbols):
  symbol_index = random.randint(0, len(symbols) - 1)
  symbol_value += symbols[symbol_index]
# Generating the symbols for the password
  
number_value = ""
for number in range(0, nr_numbers):
  number_index = random.randint(0, len(numbers) - 1)
  number_value += numbers[number_index]

combine_password = str(letter_value + symbol_value + number_value)
password_value = len(combine_password)
random_password_order = "".join(random.sample(combine_password, password_value))
 
print('\nHere is "Hard" password in a randomised order to what was requested:\n>>  ' + random_password_order)