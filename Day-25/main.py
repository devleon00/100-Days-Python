# with open("Day-25\weater_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("Day-25\weater_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp": 
#             temperatures.append(int(row[1]))
#     print(temperatures)

from hashlib import new
import pandas

data = pandas.read_csv("Day-25\weater_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(round(sum(temp_list) / len(temp_list)))
print(data.temp[data.day == "Monday"] * 1.8 + 32)

data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")


#########################################
# Squirrel Data

squirrel_data = pandas.read_csv("Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray  = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon  = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black  = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
print(len(gray.index))
print(len(cinnamon.index))
print(len(black.index))

dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [len(gray), len(cinnamon), len(black)]
}

squirrels = pandas.DataFrame(dict)
squirrels.to_csv("Day-25/squirrel_count.csv")