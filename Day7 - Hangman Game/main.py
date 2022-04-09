#My Hangman Game in Python by Allen Clarke

# Import all the module need for this code
import random
import hangman_art
import hangman_words
from os import system, name

def clear():
   # for mac and linux(here, os.name is 'posix')
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfrom
      _ = system('cls')

#Define the variables
game_word = random.choice(hangman_words.word_list)
word_length = len(game_word)
already_submitted = []
end_of_game = False
lives = 6

#Displaying the Hangman logo.
print(hangman_art.logo+"written by Allen Clarke\n")

#Create blanks holder
display = []
for char in range(word_length):
  display += "_" 

#Code to loop the until either user win or no more lives avalaible 
while not end_of_game:
    #Ask the user to enter a letter
    guess = input("Please guess a letter of the word: \n").lower()
    #Clear the screen after user submit there answer
    clear()
   
    #Check to see if the user has aleady guessed this letter.
    if guess in already_submitted:
      print(f'\nYou already guessed "{guess}" previously!\n')
    else:
      #Store user guessed letter
      already_submitted += guess
      #Check guessed letter
      for position in range(word_length):
          char = game_word[position]
          if char == guess:
              display[position] = char
  
      #Check if user is wrong.
      if guess not in game_word:
          #Let the user know what letter they have guessed wrong as well as they lose a life
          print(f'\nThis letter "{guess}" is not in the word. You lose a life!\n')
          lives -= 1
          if lives == 0:
              end_of_game = True
              #Let the use know that have lost the game and what the word was
              print('\nSorry, you lose. The word was "' + ''.join(game_word)+'"')
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("\nNice! You have won.")
  
      #Display the current stage of the hangman.
      print(hangman_art.stages[lives])