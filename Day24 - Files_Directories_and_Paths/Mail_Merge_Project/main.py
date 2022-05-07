# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
NAME_HOLDER = "[name]"

# Reading the letter content from the "starting_letter.txt" template
with open("./Input/Letters/starting_letter.txt") as letter_content:
    letter = letter_content.read()

# Reading the name listed in the "invited_names.txt"
with open("./Input/Names/invited_names.txt") as name_content:
    # appending the name into a list
    name_list = name_content.read().splitlines()

for name in name_list:
    # Replacing the name holder [name] with actual name of the guest
    name_merge_letter = letter.replace(NAME_HOLDER, name)
    # Create a new invite letter for the named guest and save it on the Output > ReadyToSend folder
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as merged_named_letter:
        merged_named_letter.write(name_merge_letter)
