# Code written by Allen Clarke
# High and lower game
# Import modules
from art import logo, vs
from game_data import data
import random
# #Only if running on replit.com
#from replit import clear

#Use on computer
from os import system, name
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfrom
      _ = system('cls')

def get_data():
  """Get data from random game data bank"""
  return random.choice(data)

def display_data(account):
  """Putting name, description and country into one list"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, list_a_followers, list_b_followers):
  """Checking with has the most follows and did the play guess the right one.""" 
  if list_a_followers > list_b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score = 0
  game_continue = True
  display_a = get_data()
  display_b = get_data()

  while game_continue:
    display_a = display_b
    display_b = get_data()

    while display_a == display_b:
      display_b = get_data()

    print(f"Compare A: {display_data(display_a)}.")
    print(vs)
    print(f"Against B: {display_data(display_b)}\n.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    list_a_follower = display_a["follower_count"]
    list_b_follower = display_b["follower_count"]
    is_correct = check_answer(guess, list_a_follower, list_b_follower)

    # #Only if running on replit.com
    #clear()
    screen_clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're correct! Your current score is: {score} \n.")
    else:
      game_continue = False
      print(f"This is the end of the game! Your scored: {score}")

game()