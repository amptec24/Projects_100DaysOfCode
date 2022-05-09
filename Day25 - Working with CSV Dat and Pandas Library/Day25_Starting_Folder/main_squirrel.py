import pandas

squirrel_colours = ["Gray", "Cinnamon", "Black"]
squirrel_dict = {"Fur Colour": ["gray", "red", "black"], "Count": []}
colour_count = 0

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# for color in squirrel_colours:
#     for count in data["Primary Fur Color"]:
#         if count == color:
#             colour_count += 1
#     squirrel_dict["Count"].append(colour_count)
#     colour_count = 0

# data = pandas.DataFrame(squirrel_dict)
# data.to_csv("squirrel_count.csv")

# Or
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
squirrel_dict = {
    "Fur Colour": ["gray", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_dataframe = pandas.DataFrame(squirrel_dict)
new_dataframe.to_csv("squirrel_count.csv")
