letter_example = ""

with open("24th_day/Mail_Merge_Project_Start/Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter_example = starting_letter.read()
    print(letter_example)

list_names:list = []

with open("24th_day/Mail_Merge_Project_Start/Input/Names/invited_names.txt") as names:
    str_names = names.read()
    list_names = str_names.split()
    print(str_names)

for name in list_names:
    personal_letter = letter_example.replace("[name]",name)
    with open(f"./24th_day/Mail_Merge_Project_Start/Output/ReadyToSend/{name}_mail.txt","w") as new_file:
        new_file.write(personal_letter)
        new_file.close()