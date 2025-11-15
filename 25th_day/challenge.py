import csv
import pandas

data = pandas.read_csv("./25th_day/squirrel_info.csv")

black_squirrel_count = data[data["Primary Fur Color"]=="Black"]["Primary Fur Color"].count()
cinammon_squirrel_count = data[data["Primary Fur Color"]=="Cinnamon"]["Primary Fur Color"].count()
gray_squirrel_count = data[data["Primary Fur Color"]=="Gray"]["Primary Fur Color"].count()

data_dict = {
    "Fur color":["Black","Cinnamon","Gray"],
    "Count":[black_squirrel_count,cinammon_squirrel_count,gray_squirrel_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("./25th_day/squirrel_count.csv")
print(data_frame)