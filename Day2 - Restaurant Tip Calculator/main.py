# Creating a Tip Calculator by Allen Clarke.
# My code below this line
print("Welcome to the tip calculator.")

# Capturing total of the bill
bill = float(input("What was the total bill? £"))

# Capturing the tip amount
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_added = 1 +(tip / 100)

# Capturing the total number of person to split the bill amount
people = int(input("How many people to split the bill amount? "))

# Calculate total what each person will pay
total_bill = (bill * tip_added) / people
# Use this if no format is needed bill_per_person = round(total_bill, 2)
bill_per_person = "{:.2f}".format(total_bill)

# Final bill per person
print(f"Each person should pay: £{bill_per_person}")