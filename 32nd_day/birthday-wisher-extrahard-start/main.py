##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random as rd
import pandas as pn

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now_date = dt.datetime.now()
now_day = now_date.day
now_month = now_date.month
now_year = now_date.year
print(now_date)

birthdays = pn.read_csv("32nd_day\\birthday-wisher-extrahard-start\\birthdays.csv")
birthdays_df = pn.DataFrame(birthdays)

def check_birthday(now_day,now_month,birthdays_df):

    result = False
    name = ""
    email = ""
    for row in birthdays_df.itterrows():
        if int(row.month) == now_month and int(row.day)==now_day:
            result = True
            name = row["name"]
            email = row["email"]
            print(f"email: f{email} | name: {name}")


check_birthday(now_day,now_month,birthdays_df)
print(birthdays_df)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




