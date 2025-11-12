with open("C:/Users/stani/Desktop/Python/100_days_of_python/24th_day/my_file.txt", mode="r") as file: # used for safety of Resource Management 
    contents = file.read()
    print(contents)

# with open("C:/Users/stani/Desktop/Python/100_days_of_python/24th_day/my_file.txt", mode="w") as file: # used for safety of Resource Management 
#     file.write("\n New text!!!")

with open("../../../Desktop/my_file.txt", mode="r") as file: # used for safety of Resource Management 
    contents = file.read()
    print(contents)