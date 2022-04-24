rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line
import random
# Randomly generating a number selection for the computer
computer_selection = random.randint(0,2)
print("Welcome to my rock paper scissors Game. \n")
player1_selection = int(input("Please enter 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


# Player 1 selected rock
if player1_selection == 0:
  if computer_selection == 0:
    print(rock)
    print("Complete chose:")
    print(rock)
    print("Draw game! You want to try again.")
  elif computer_selection == 1:
    print(rock)
    print("Computer chose:")
    print(paper)
    print("Computer won!")
  else:
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You won!")
    
# Player 1 selected paper
elif player1_selection == 1:
  if computer_selection == 0:
    print(paper)
    print("Complete chose:")
    print(rock)
    print("You won!")
  elif computer_selection == 1:
    print(paper)
    print("Computer chose:")
    print(paper)
    print("Draw game! You want to try again.")
  else:
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("Computer won!")
    
# Player 1 selected scissors
elif player1_selection == 2:
  if computer_selection == 0:
    print(scissors)
    print("Complete chose:")
    print(rock)
    print("Computer won!")
  elif computer_selection == 1:
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You won!")
  else:
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("Draw game! You want to try again.")
else:
  print("Game over! Please select between rock, paper or scissors.")
print("\nThank you for playing code written by Allen Clarke")