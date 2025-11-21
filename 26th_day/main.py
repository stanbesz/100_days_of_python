# numbers = [1,2,3]
# new_list = []
# for num in numbers:
#     new_l = num +1
#     new_list.append(new_l)

# print(new_list)

# The above can be replaced by

import random
import pandas

numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
new_list_name = [letter for letter in name]
print(new_list_name)

new_range = [n*2 for n in range(1,5)]
print(new_range)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]

upper_names = [name.upper() for name in names if len(name)>5]
print(upper_names)

students_score = {student:random.randint(1,100) for student in names}
print(students_score)

passed_student = {student:value for (student,value) in students_score.items() if value > 60}
print(passed_student)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_sentence = sentence.split()
result = {word:len(word) for word in list_sentence}
print(result)


studen_dict = {"student":["Angela","James","Lily"],
               "score":[56,76,98]}

student_data_frame = pandas.DataFrame(studen_dict)
print(student_data_frame)

#Loop through a data frame
# for key,value in student_data_frame.items():
#     print(key,value)

#Loop through rows of data frame
for index,row in student_data_frame.iterrows():
    print("Index: ",index)
    print("Row student: ",row.student)
    print("Row score: ",row.score)
    if row.student == "Angela":
        print(row.score)