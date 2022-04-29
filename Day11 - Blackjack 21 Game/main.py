# Blackjack 21 written by Allen Clarke
# Import modules
import random
#from replit import clear
from os import system, name
from art import logo

# Define functions
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfrom
      _ = system('cls')

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, dealer_score):
  """Comparing score of player vs dealer"""
  if player_score > 21 and dealer_score > 21:
    return "\nYour score is greater than 21. You lose!\n"
  elif player_score == dealer_score:
    return "\nIts a draw!\n"
  elif dealer_score == 0:
    return "\nYou lose! Dealer has Blackjack\n"
  elif player_score == 0:
    return "\nYou won! You have Blackjack\n"
  elif player_score > 21:
    return "\nYour score is greater than 21. You lose!\n"
  elif dealer_score > 21:
    return "\nDealer score is greater than 21. You win!\n"
  elif player_score > dealer_score:
    return "\nYou won!\n"
  else:
    return "\nYou lose!\n"
    
def play_game():
  #Game logo
  print(logo)
  
  #Game variables
  dealer_cards = []
  player_cards = []
  is_game_over = False

  # Game dealing card and adding to cards to both player and dealer
  for game in range(2):
    dealer_cards.append(deal_card())
    player_cards.append(deal_card())

  while not is_game_over:
    dealer_score = calculate_score(dealer_cards)
    player_score = calculate_score(player_cards)  
    print(f"   Dealer's first card: {dealer_cards[0]}")
    print(f"   Your cards: {player_cards}, current score: {player_score}")

    if dealer_score == 0 or player_score == 0 or player_score > 21:
      is_game_over = True
    else:
      user_hit = input("\nType 'y' to get another card, type 'n' to pass: ").lower()
      if user_hit == "y":
        player_cards.append(deal_card())
      else:
        is_game_over = True

  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)

  print(f"\n   Your final hand: {player_cards}, final score: {player_score}")
  print(f"   Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(player_score, dealer_score))    
  
while input("Would you like to play my simple Blackjack game? Type 'y' or 'n': ").lower() == "y":
  screen_clear()
  play_game()
else:
  print("\nGoodbye!")


