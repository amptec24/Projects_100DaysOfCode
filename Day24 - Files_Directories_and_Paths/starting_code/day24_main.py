# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # mode w = overwrite, a = append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

# # Create a new file if it does not exist
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew text.")

# # Getting the file save on my desktop using absolute file path
# with open("/Users/your_name/Desktop/desk_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Getting the file save on my OneDrive using absolute file path
with open("../../../desk_file.txt") as file:
    contents = file.read()
    print(contents)
