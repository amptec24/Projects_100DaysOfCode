#import os
from os import system, name
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfrom
      _ = system('cls')
   # print out some text
print("The platform is: ", name)
print("big output\n"* 5)
# wait for 5 seconds to clear screen
sleep(5)
# now call function we defined above
screen_clear()