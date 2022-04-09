#Import all the module needed
#from replit import clear
from art import logo
from os import system, name

#Define variables
end_of_bids = False
bids = {}

#Define a calculating winner function
def clear():
   # for mac and linux(here, os.name is 'posix')
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfrom
      _ = system('cls')

def find_winner(bid_values):
  highest_bid = 0
  winner = ""
  for bidder in bid_values:
    bid_amount = bid_values[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"Congratulations! The winner is {winner} with a bid of £{highest_bid}!")

#Display logo at the start of the game
print(logo)
print("\nWelcome to the my secret auction program, lets start!")

#Main code 
while not end_of_bids:  
    name = input("What is your name?\n")
    bid = int(input("What's your bid?:\n£"))
    bids[name] = bid
   
    other_bidders = input("\nAre there any other bidders? Type 'Yes' or 'No'\n").lower()
    #Check if the user want to end bidding
    if other_bidders == "no":
      end_of_bids = True
      clear() 
      find_winner(bids)
    elif other_bidders == "yes":
      clear()