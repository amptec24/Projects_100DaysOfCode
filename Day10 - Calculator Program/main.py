# Code written bbby Allen Clarke

#Import the module needed
#from replit import clear
from art import logo
from os import system, name

# Function for the calculator
def clear():
   # for mac and linux(here, os.name is 'posix')
   if name == 'posix':
      _ = system('clear')
   else:
      # for windows platfrom
      _ = system('cls')

def add(n1,n2):
  """To add n1 to n2"""
  return n1 + n2

def subtract(n1,n2):
  """To subtract n1 to n2"""
  return n1 - n2

def multiply(n1,n2):
  """To multiply n1 to n2"""
  return n1 * n2

def divide(n1,n2):
  """To add n1 to n2"""
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  
}

def calculator():
  print(logo)
  num1 = float(input("Enter your first number?: "))
  for symbol in operations:
    print(symbol)
  
  contine_calculation = True
  
  while contine_calculation:    
    operations_symbol = input("Pick an operation ")
    num2 = float(input("Enter your next number?: "))
    calculator_function = operations[operations_symbol]
    answer = calculator_function(num1,num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
  
    another_calculation = input(f"Type 'Y' to continue calculating with {answer}, or type 'N' to start a new calculation!\n").lower()
    if another_calculation == "y":
      num1 = answer
    elif another_calculation == "n":
      contine_calculation = False
      clear()
      calculator()

calculator()