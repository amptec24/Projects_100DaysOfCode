#Number guessing game written by Allen Clarke
#importing modules
from random import randint
from art import logo

#Choosing a randon nuymber between 1 and 100.
computer_number = randint(1, 101)
game_level = {"easy": 10, "hard": 5}

#Comparing numbers functions
def compare(guessed_number):
    if guessed_number > computer_number:
        return "Too high!"
    elif guessed_number < computer_number:
        return "Too low!"
    elif guessed_number == computer_number:
        return "matched"

#Playing Game function
def game():
  play_game = True
  print(logo)
  print("Welcome to the My Number Guessing Game!")
  print("I am think about a number between 1 and 100")
  player_level = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
  game_rounds = game_level[player_level]
  
  while play_game:
      print(f"\nYou have {game_rounds} attempts remaining to guess the number.")
      number_guessed = int(input("Make a guess: "))
      print(compare(number_guessed))
      game_rounds -= 1
  
      if compare(number_guessed) == "matched":
          print("\nYou guessed it. You won!")
          play_game = False
      elif game_rounds == 0:
          print(
              f"\nSorry, you ran out of guesses. The number was {computer_number}, Thank you for playing."
          )
          return
      else:
        print("Guess again")

game()