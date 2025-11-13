# list_weather:list = []

# with open("./25th_day/weather_data.csv","r") as file:
#     list_temp = file.readlines()
#     for day in list_temp:
#         temp = day.strip()
#         list_weather.append(temp)

# print(list_weather)

import csv
import pandas

with open("./25th_day/weather_data.csv","r") as file:
    data = csv.reader(file)
    temperatures:list = []
    for row in data:
        if row[1].isnumeric():
            temperatures.append(int(row[1]))
        else:
            pass
        print(row)

    for temp in temperatures:
        print(temp)

data = pandas.read_csv("./25th_day/weather_data.csv")
data_dict = data.to_dict()
# print(data_dict)
temp_list = data["temp"].to_list()

temp_list_average = sum(temp_list) / len(temp_list)

print(f"Avg: {temp_list_average}")
print("Mean: ",data["temp"].mean())
print("Max: ",data["temp"].max())

print(data.temp)
print(data[data.day=="Monday"])
print(data[data.temp == data["temp"].max()])

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores":[76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./25th_day/new_data.csv")