sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
#  The method be split() the sentence into word in a list
result = {word:len(word) for word in sentence.split()}

print(result)
