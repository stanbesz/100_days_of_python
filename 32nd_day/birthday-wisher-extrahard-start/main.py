##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random as rd
import pandas as pn
from collections import defaultdict
from pathlib import Path

my_email = "stanbesz503@gmail.com"
password = "ifel zjzp drno kdhk"

now_date = dt.datetime.now()
now_day = now_date.day
now_month = now_date.month
now_year = now_date.year

birthdays = pn.read_csv("32nd_day\\birthday-wisher-extrahard-start\\birthdays.csv")
birthdays_df = pn.DataFrame(birthdays)
birthday_map:dict = defaultdict(list)

birthday_letters:list = []

folder = Path("32nd_day\\birthday-wisher-extrahard-start\letter_templates")

birthday_letters = [file.read_text(encoding="utf-8") for file in folder.glob("*.txt")]

for _,row in birthdays_df.iterrows():
    birthday_map[(row.day, row.month)].append((row["name"],row.email))

def send_birthday_mail(name,email,birthday_letters):
    birthday_letter = rd.choice(birthday_letters)
    name_letter = birthday_letter.replace("[NAME]",name)

    with smtplib.SMTP("smtp.gmail.com") as connection: # Same as the file reading/writing
        connection.starttls() #make connection secure
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject: Happy Birthday {name} \n\n {name_letter}")

def send_emails(now_day,now_month,birthday_letters,birthday_map):

    check_birthday = (now_day,now_month) in list(birthday_map.keys())

    if check_birthday:
        for person in birthday_map[(now_day,now_month)]:
            send_birthday_mail(person[0],person[1],birthday_letters)
    else:
        print("No birthdays Today!")

send_emails(now_day,now_month,birthday_letters,birthday_map)