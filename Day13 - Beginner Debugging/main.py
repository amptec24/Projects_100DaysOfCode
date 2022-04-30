# Code written by Allen Clarke
# 1.Debugging Odd and Even
number = int(input("Which number do you want to check?: "))

# if number % 2 = 0:
# The a above if statement was set the number % 2 as 0 and check to see if it was equal to 0
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

###################################################
# 2.Debugging Leap Year
# year = input("Which year do you want to check?")
# the above code is take the string input from the use divide it by an int therefore, it will error out. We need to conver the string to an int by adding int()
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

###################################################
# 3.Debugging FizzBuzz
for number in range(1, 101):
  # if number % 3 == 0 or number % 5 == 0:
  # Worng operator was used and should be used instead of or as you want both condisition to be true not just one 
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # if number % 3 == 0:
  # Missing the elif statement 
  elif number % 3 == 0:
    print("Fizz")
  # if number % 5 == 0:
  # Missing the elif statement 
  elif number % 5 == 0:
    print("Buzz")
  else:
    # print([number]).
    # remove the sqaure braket[]
    print(number)