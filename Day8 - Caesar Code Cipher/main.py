#Caesar Code Cipher written by Allen Clarke
#Import all the module need
from code import alphabet
from art import logo

# Define the caesar() function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

#Print the logo when the program starts.
print(logo)

#Varible to end program
should_end = False

#Code for encoding and decoding the message
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #To ensure user does not enter more characters that the alphabet
  shift = shift % 26

  #Passing the argument to the parameter to print encoded or decoded message
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  #check if the user wants to continue the program or not
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("\nGoodbye")