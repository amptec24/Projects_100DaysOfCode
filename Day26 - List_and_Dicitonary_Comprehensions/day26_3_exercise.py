with open("file1.txt") as data1:
    f1 = data1.readlines()

with open("file2.txt") as data2:
    f2 = data2.readlines()

result = [int(num) for num in f1 if num in f2]
# Write your code above 👆

print(result)
