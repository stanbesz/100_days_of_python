import smtplib
import datetime as dt
import random as rd

#---------------------------Datetime---------------------#
now = dt.datetime.now()
weekdays:list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day_of_week = now.weekday()
if now == day_of_week:
    print("Hello???")
else:
    print("Huh???")
#---------------------------Quotes-----------------------#
list_quotes:list = []

with open("32nd_day\quotes.txt","r") as file:
    list_quotes=file.readlines()

quote_of_day = rd.choice(list_quotes)
# print(quote_of_day)
#---------------------------Mail Logic---------------------#

my_email = "stanbesz503@gmail.com"
password = "ifel zjzp drno kdhk"

with smtplib.SMTP("smtp.gmail.com") as connection: # Same as the file reading/writing
    connection.starttls() #make connection secure
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="stanbe_sz@abv.bg",msg=f"Subject: Motivational Quote for {weekdays[day_of_week]} \n\n {quote_of_day}")
    # connection.close()
# Saves connection.close()
