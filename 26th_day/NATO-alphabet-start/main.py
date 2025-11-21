student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


alphabet = pandas.read_csv("26th_day/NATO-alphabet-start/nato_phonetic_alphabet.csv").to_dict()
alphabet_data_frame = pandas.DataFrame(alphabet)
alpha_mapped = {row.letter:row.code for index,row in alphabet_data_frame.iterrows()}

print(alpha_mapped)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
list_user_name = [alpha_mapped[letter] for letter in user_input]
print(list_user_name)

