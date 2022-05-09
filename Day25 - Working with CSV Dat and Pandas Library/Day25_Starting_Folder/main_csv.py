# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# # Working to  python building CSV library
# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     weather_data = list(data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# Create our data frame
data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])

# Getting the list of the temperatures in th temp column
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

#  Calculating the average of temperatures in th temp column
average = data["temp"].mean()
print(average)

# Finding the maximum temperature in the temp column
max_temp = data["temp"].max()
print(max_temp)

#  Get Data in Column
print(data["condition"])
print(data.condition)

# Get Data in row
print(data[data["day"] == "Monday"])
# or
print(data[data.day == "Monday"])

# Challenge: print the row of data which had the highest temperature
print(">> Challenge: which row had the highest temperature")
print(data[data.temp == data.temp.max()])

# Print a column in a row
monday = data[data.day == "Monday"]
print(monday.condition)

# Challenge: print Monday's temperature from 'C to 'F
print(">> Challenge: Print Monday's temperature from 'C to 'F")
monday = data[data.day == "Monday"]
temp_in_fah = float((monday.temp * (9/5)) + 32)
print(f"Monday's temperature was {temp_in_fah}'F")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Allen"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")