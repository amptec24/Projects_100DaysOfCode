import random
# Working with "List Comprehension"
# new_number = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(numbers)
print(new_list)

# letter_list = [letter for letter in name]
name = "Allen"
new_list_letter = [letter for letter in name]
print(name)
print(new_list_letter)

new_range_list = [n * 2 for n in range(1, 5)]
print(new_range_list)

# Working with "Conditional List Comprehension"
# new_number = [new_item for item in list if test]
names = ["Alex", "Beth", "Coraline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)
print(upper_names)


# Working with "Dictionary Comprehension"
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
names = ["Alex", "Beth", "Coraline", "Dave", "Eleanor", "Freddie"]

students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
# Get student that name and scores that are 60% and above
passed_student = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_student)
