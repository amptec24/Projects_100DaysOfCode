import pandas

student_dict = {
    "student": ["Allen", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Looping through data frame:
# for (key, value) in student_data_frame.items():
#     # print(key)
#     print(value)

# Looping through rows of data frame:
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    if row.student == "Allen":
        print(row.score)
